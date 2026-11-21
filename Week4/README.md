# WEEK 4 – Tokenizer Lab: BPE, WordPiece and SentencePiece

## 1. Aim

To compare different tokenization techniques such as BPE, WordPiece, and SentencePiece using English, Telugu, and Hindi sentences, and analyze their tokens, token IDs, and token counts.

## 2. Technologies Used

- Python
- Hugging Face Transformers
- BPE (GPT-2)
- WordPiece (Multilingual BERT)
- SentencePiece (XLM-R)
- Pandas

## 3. Folder Structure

WEEK4/
├── WEEK4_Tokenizer_Lab_BPE_WordPiece_SentencePiece.ipynb
└── README.md

## 4. Installation

Open the WEEK4 notebook in Google Colab.

Install dependencies:

!pip install transformers sentencepiece

## 5. Configuration

Import the required library:

from transformers import AutoTokenizer

Define the three tokenizers:

BPE - GPT-2:
gpt2

WordPiece - Multilingual BERT:
bert-base-multilingual-cased

SentencePiece - XLM-R:
xlm-roberta-base

## 6. Implementation Steps

1. Install Transformers and SentencePiece libraries.
2. Import AutoTokenizer.
3. Define BPE, WordPiece, and SentencePiece tokenizers.
4. Prepare sample sentences in English, Telugu, and Hindi.
5. Load all three pretrained tokenizers.
6. Convert sentences into tokens.
7. Generate token IDs.
8. Calculate token counts.
9. Compare the tokenization results using a Pandas DataFrame.

## 7. Execution

Run all notebook cells in Google Colab.

The program loads the three tokenizers and processes the input sentences.

## 8. Sample Input

English:
Artificial intelligence is changing the world.

Telugu:
కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.

Hindi:
कृ त्रिम बुद्धिमत्ता दुनिया को बदल रही है।

## 9. Expected Output

The notebook displays:

- Generated tokens
- Token IDs
- Token counts
- Tokenizer comparison table

The comparison table contains:

Language
BPE - GPT-2
WordPiece - Multilingual BERT
SentencePiece - XLM-R

## 10. Result

Successfully compared BPE, WordPiece, and SentencePiece tokenization methods using English, Telugu, and Hindi text and analyzed their tokens, token IDs, and token counts.

