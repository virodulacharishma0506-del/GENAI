# WEEK 6 – LLM Evaluation using Golden Set and Baseline Results

## 1. Aim

To evaluate Large Language Model (LLM) responses using a Golden Set dataset and Baseline Results by comparing generated answers with expected answers, matching keywords, calculating scores, and identifying PASS or REVIEW status.

## 2. Technologies Used

- Python
- JSON
- CSV
- Requests
- Llama 3.2
- Keyword Matching
- Baseline Evaluation

## 3. Folder Structure

WEEK6/
├── golden_set.json
├── baseline_results.csv
├── requirements.txt
└── README.md

## 4. Installation

Activate the shared virtual environment:

cd C:\GENAI
.\venv\Scripts\Activate.ps1

Navigate to Week 6:

cd PRACTICAL\WEEK6

Install dependencies:

pip install -r requirements.txt

## 5. Configuration

The project uses two important files:

1. golden_set.json

Contains 30 evaluation questions with:

- Question ID
- Question
- Expected Answer
- Keywords
- Source Reference

2. baseline_results.csv

Contains baseline evaluation information with:

- Question ID
- Question
- Expected Answer
- LLM Answer
- Matched Keywords
- Missing Keywords
- Score
- Status
- Source
- Model
- Release

Model Used:

llama3.2

Release:

v0.1

## 6. Implementation Steps

1. Prepare a Golden Set containing evaluation questions.
2. Define expected answers for each question.
3. Identify important keywords for every question.
4. Store the questions in JSON format.
5. Use LLM-generated answers as baseline responses.
6. Compare generated answers with expected answers.
7. Identify matched keywords.
8. Identify missing keywords.
9. Calculate evaluation scores.
10. Assign PASS or REVIEW status.
11. Store the baseline evaluation results in CSV format.

## 7. Execution

The uploaded project contains the Golden Set and Baseline Results datasets.

To inspect the Golden Set:

python -c "import json; print(len(json.load(open('golden_set.json', encoding='utf-8'))))"

To inspect the CSV file:

python -c "import csv; f=open('baseline_results.csv', encoding='utf-8-sig'); print(next(csv.reader(f)))"

Note: The uploaded files do not include a Python evaluation script for generating new baseline results.

## 8. Sample Input

Question:

What is tokenization in large language models?

Expected Answer:

Tokenization is the process of splitting input text into smaller units called tokens.

Keywords:

- splitting
- text
- tokens

## 9. Expected Output

The project provides baseline evaluation results containing:

- Expected answers
- LLM-generated answers
- Matched keywords
- Missing keywords
- Evaluation scores
- PASS or REVIEW status

Baseline Dataset Summary:

Total Questions: 30

PASS: 12

REVIEW: 18

Model: llama3.2

Release: v0.1

## 10. Result

Successfully organized a Golden Set dataset and baseline LLM evaluation results to analyze generated answers using expected answers, keyword matching, evaluation scores, and PASS or REVIEW status.

