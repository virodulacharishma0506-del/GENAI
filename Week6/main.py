
import json
import csv
import requests
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

INPUT_FILE = "golden_set.json"
OUTPUT_FILE = "baseline_results.csv"


def get_llm_answer(question):
    payload = {
        "model": MODEL_NAME,
        "prompt": question,
        "stream": False,
        "options": {
            "temperature": 0,
            "num_predict": 100
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    return response.json()["response"]


def calculate_score(answer, expected_keywords):
    answer_lower = answer.lower()

    matched = [
        word for word in expected_keywords
        if word.lower() in answer_lower
    ]

    missing = [
        word for word in expected_keywords
        if word.lower() not in answer_lower
    ]

    if not expected_keywords:
        score = 0
    else:
        score = (
            len(matched) / len(expected_keywords)
        ) * 100

    return round(score, 2), matched, missing


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        questions = json.load(file)

    results = []

    total_score = 0
    successful = 0
    passed = 0
    review = 0
    errors = 0

    print("Starting baseline evaluation...")
    print("Model:", MODEL_NAME)
    print("Total questions:", len(questions))

    for item in questions:

        question_id = item["id"]
        question = item["question"]

        print("\nProcessing", question_id)

        try:
            answer = get_llm_answer(question)

            score, matched, missing = calculate_score(
                answer,
                item["keywords"]
            )

            status = "PASS" if score >= 60 else "REVIEW"

            successful += 1
            total_score += score

            if status == "PASS":
                passed += 1
            else:
                review += 1

            print("Score:", score)
            print("Status:", status)

        except Exception as error:

            answer = ""
            score = 0
            matched = []
            missing = item["keywords"]
            status = "ERROR"

            errors += 1

            print("Error:", error)

        results.append({
            "Question_ID": question_id,
            "Question": question,
            "Expected_Answer": item["expected_answer"],
            "LLM_Answer": answer,
            "Matched_Keywords": ", ".join(matched),
            "Missing_Keywords": ", ".join(missing),
            "Score": score,
            "Status": status,
            "Source": item["source"],
            "Model": MODEL_NAME,
            "Release": "v0.1"
        })

    fieldnames = [
        "Question_ID",
        "Question",
        "Expected_Answer",
        "LLM_Answer",
        "Matched_Keywords",
        "Missing_Keywords",
        "Score",
        "Status",
        "Source",
        "Model",
        "Release"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    average_score = (
        round(total_score / successful, 2)
        if successful else 0
    )

    print("\n========== RELEASE v0.1 ==========")
    print("Model:", MODEL_NAME)
    print("Total Questions:", len(questions))
    print("Successful Responses:", successful)
    print("Passed:", passed)
    print("Review:", review)
    print("Errors:", errors)
    print("Average Keyword Coverage:", average_score, "%")
    print("Date:", datetime.now())
    print("Results saved to:", OUTPUT_FILE)
    print("Baseline evaluation completed!")


if __name__ == "__main__":
    main()
