
WEEK 8 – Multi-Head Attention and Causal Masking
1. Aim
To implement Scaled Dot-Product Attention and Multi-Head Attention using PyTorch, understand self-attention, and demonstrate causal masking in GPT-style models.
2. Technologies Used
- Python
- PyTorch
- Torch.nn
- Torch.nn.functional
- Google Colab
- Scaled Dot-Product Attention
- Multi-Head Attention
- Causal Masking
3. Folder Structure
WEEK8/
│
└── Week8.ipynb


4. Installation
Open the Week 8 notebook in Google Colab.

PyTorch is used for tensor operations, neural network layers, and attention calculations.

If PyTorch is not installed, execute:
!pip install torch



5. Configuration
The notebook uses the following parameters:
Parameter	Value
Batch size	1
Sequence length	3
Embedding dimension (d_model)	4
Number of attention heads	4
Dimension per head (d_k)	1

The input embeddings are generated using:
torch.manual_seed(42)x = torch.randn(batch_size, seq_len, d_model)



6. Implementation Steps
1. Import math and PyTorch libraries.
2. Implement the scaled_dot_product_attention() function.
3. Calculate attention scores using Query (Q), Key (K), and Value (V).
4. Apply scaling using the square root of the key dimension.
5. Apply masking when a mask is provided.
6. Calculate attention weights using Softmax.
7. Create the MultiHeadAttention class.
8. Implement Query, Key, Value and Output linear projections.
9. Split the embeddings into multiple attention heads.
10. Combine the attention heads.
11. Perform unmasked self-attention.
12. Implement causal masking using a lower-triangular matrix.
13. Display attention weights and output shapes.
7. Execution
Run Cell 1 – Imports & Scaled Dot-Product Attention
Execute the first cell to import libraries and define the scaled attention function and Multi-Head Attention class.
Run Cell 2 – Multi-Head Attention Module
Execute the second cell to define the Multi-Head Attention module, including splitting and combining heads.
Run Cell 3 – Test Self-Attention & Causal Masking
Execute the final cell to perform both tests:
- Unmasked Self-Attention (Encoder-style)
- Causal Masking (Decoder/GPT-style)
8. Sample Input
Parameter	Value
Batch size	1
Sequence length	3
Embedding dimension	4
Number of heads	4
Input	Randomly generated tensor
Random seed	42

9. Expected Output
The program displays the following:
Test 1 – Unmasked Self-Attention
- Input shape
- Output shape
- Attention weights shape
- Attention weight values
- Attention output values
Expected tensor shapes
Input shape:             torch.Size([1, 3, 4])
Output shape:            torch.Size([1, 3, 4])
Attention weights shape:  torch.Size([1, 4, 3, 3])


Test 2 – Causal Masking
- Input shape
- Number of attention heads
- Masked attention weights
- Multi-head attention output
- Final output shape
Input Shape: torch.Size([1, 3, 4])
Number of Heads: 4
Attention Weights Shape: torch.Size([1, 4, 3, 3])
Output Shape: torch.Size([1, 3, 4])


Checks
Test	Expected
Unmasked Self-Attention	PASS
Multi-Head Attention	PASS
Causal Masking	PASS
Output shape validation	PASS

10. Result
Successfully implemented Scaled Dot-Product Attention and Multi-Head Attention using PyTorch. Tested self-attention with and without causal masking, and observed the attention weights and output tensors.
