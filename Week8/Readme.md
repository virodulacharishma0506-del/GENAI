# WEEK 8 – Multi-Head Attention and Causal Masking

## 1. Aim

To implement Scaled Dot-Product Attention and Multi-Head Attention using PyTorch, understand self-attention, and demonstrate causal masking in GPT-style language models.

## 2. Technologies Used

- Python
- PyTorch
- Torch.nn
- Torch.nn.functional
- Google Colab
- Jupyter Notebook

## 3. Folder Structure

```text
WEEK8/
│
├── Week8.ipynb
└── README.md
```

## 4. Installation

Open the `Week8.ipynb` notebook in Google Colab.

Install the required library if it is not already available:

```python
!pip install torch
```

Import the required modules:

```python
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
```

## 5. Configuration

The following parameters are used in the experiment:

| Parameter | Value |
|---|---:|
| Batch Size | 1 |
| Sequence Length | 3 |
| Embedding Dimension | 4 |
| Number of Attention Heads | 4 |
| Dimension per Head | 1 |
| Random Seed | 42 |

Input tensor generation:

```python
torch.manual_seed(42)
x = torch.randn(batch_size, seq_len, d_model)
```

## 6. Implementation Steps

1. Import the required Python and PyTorch libraries
