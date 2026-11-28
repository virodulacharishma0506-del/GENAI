
# WEEK 7 – Next-Token Prediction Using DistilGPT-2

## 1. Aim

To implement a next-token prediction system using the DistilGPT-2 language model, understand tokenization, perform forward propagation, calculate token probabilities using Softmax, and identify the Top-K most probable next tokens.

## 2. Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- DistilGPT-2
- AutoTokenizer
- AutoModelForCausalLM
- Softmax
- Google Colab

## 3. Folder Structure

```text
WEEK7/
│
├── Week_7.ipynb
└── README.md
```

## 4. Installation

Open the `Week_7.ipynb` notebook in Google Colab.

Install the required libraries:

```python
!pip install -q transformers torch
```

## 5. Configuration

The experiment uses the DistilGPT-2 pretrained language model.

Model configuration:

```python
model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

model.eval()
```

### Model Details

| Parameter | Value |
|---|---|
| Model | DistilGPT-2 |
| Vocabulary Size | 50,257 tokens |
| Framework | PyTorch |
| Pretrained Model Source | Hugging Face |
| Task | Next-Token Prediction |

## 6. Implementation Steps

1. Install the required Transformers and PyTorch libraries.
2. Import the required Python modules.
3. Load the DistilGPT-2 pretrained model.
4. Load the corresponding tokenizer.
5. Set the model to evaluation mode.
6. Define the `inspect_next_tokens()` function.
7. Convert the input prompt into token IDs using the tokenizer.
8. Perform a forward pass through the model.
9. Extract the next-token logits.
10. Apply Softmax to convert logits into probabilities.
11. Identify the Top-K most probable next tokens using `torch.topk()`.
12. Display token rank, token text, token ID, raw logit and probability.

## 7. Execution

Open `Week_7.ipynb` in Google Colab and execute all cells in order.

### Cell 1 – Install Required Libraries

Install Transformers and PyTorch.

```python
!pip install -q transformers torch
```

### Cell 2 – Load Tokenizer and Model

Load the DistilGPT-2 model and tokenizer.

Display the model name and vocabulary size.

### Cell 3 – Next-Token Prediction Function

Define the `inspect_next_tokens()` function to:

- Tokenize the input prompt.
- Perform model inference.
- Extract logits.
- Calculate Softmax probabilities.
- Display the Top-K predicted tokens.

### Cell 4 – Classroom Exercise 1

Execute the following prompt:

```python
inspect_next_tokens("Water boils at 100 degrees", top_k=5)
```

### Cell 5 – Classroom Exercise 2

Execute the following prompt:

```python
inspect_next_tokens("Once upon a time, there was a", top_k=5)
```

## 8. Sample Input

### Input 1 – Factual Sentence

```text
The capital of France is
```

### Input 2 – Scientific Sentence

```text
Water boils at 100 degrees
```

### Input 3 – Creative Sentence

```text
Once upon a time, there was a
```

## 9. Expected Output

The program displays a TOKEN PREDICTION REPORT containing:

- Input prompt
- Predicted token rank
- Token text
- Token ID
- Raw logit
- Softmax probability

### Sample Output – Water Prediction

```text
Prompt: 'Water boils at 100 degrees'

Rank   Token          Token ID   Raw Logit    Probability
--------------------------------------------------------------
1      Fahrenheit     35935      -58.9696     0.22
2      ,              11         -59.3260     0.15
3      Celsius        34186      -59.4020     0.14
4      .              13         -59.7986     0.09
5      and            290        -60.1684     0.07
```

### Verification

| Component | Expected Result |
|---|---|
| Model Loading | PASS |
| Tokenization | PASS |
| Forward Pass | PASS |
| Logit Extraction | PASS |
| Softmax Calculation | PASS |
| Top-K Prediction | PASS |

## 10. Result

Successfully implemented a next-token prediction system using the DistilGPT-2 language model. Loaded the tokenizer and pretrained model, performed forward inference, calculated Softmax probabilities, and identified the Top-K predicted tokens for factual, scientific, and creative text prompts.

---

**Author:** Charishma Virodula

**Project:** Week 7 – Next-Token Prediction Using DistilGPT-2
