# WEEK 2 – Provider-Agnostic LLM Client

## Aim

To develop a provider-agnostic LLM client using Python that supports multiple AI providers, including Google Gemini API and a locally running Ollama model, through a common interface.

## Technologies Used

- Python
- Google Gemini API
- Ollama
- Qwen 2.5 (0.5B Model)
- Requests
- Python Virtual Environment

## Tools Used

- Python
- Visual Studio Code
- Gemini API
- Ollama

## Folder Structure

```text
WEEK2/
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
├── .env
├── Modelfile
└── README.md
```

## Installation Steps

1. Install Python on your system.

2. Install Ollama on your system.

3. Open the WEEK2 folder in VS Code.

4. Create and activate a virtual environment:

```bash
python -m venv myenv
myenv\Scripts\activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Download the Ollama model:

```bash
ollama pull qwen2.5:0.5b
```

7. Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

**Note:** Never upload your actual API key to GitHub.

## Execution Steps

Run the following command in the terminal:

```bash
python main.py
```

1. The program starts and asks the user to select an AI provider.
2. Select Gemini or Ollama.
3. Enter a prompt or question.
4. The prompt is sent to the selected LLM provider.
5. The selected model generates a response.
6. The response is displayed in the terminal.

To test the application, run:

```bash
python -m unittest test_client.py
```

## Expected Output

The program accepts a prompt and generates an AI response using either Gemini or Ollama.

**Example:**

Input:
```text
Explain Artificial Intelligence.
```

Output:
```text
Artificial Intelligence is a technology
that enables machines to perform tasks
that normally require human intelligence.
```

## Result

Successfully developed a provider-agnostic LLM client using Python that supports both Google Gemini API and the locally running Ollama model through a common interface.

