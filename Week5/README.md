
# WEEK 5 – Token Economics: Cost and Rate Limit Budgeting

## 1. Aim

To develop a Token Economics and Budgeting application using Python that estimates token consumption, calculates API usage costs, evaluates rate limits, and checks daily and monthly budget constraints.

## 2. Technologies Used

- Python
- Python-dotenv
- Environment Variables (.env)
- Dataclasses
- Unit Testing (unittest)

## 3. Folder Structure

WEEK5/
├── WEEK5_Token_Economics.ipynb
├── budget.py
├── test_budget.py
├── .env
└── README.md

## 4. Installation

Open the WEEK5 notebook in Google Colab.

Install the required package:

!pip install python-dotenv

## 5. Configuration

Create a .env file and configure the following values:

INPUT_PRICE_PER_MILLION=0.30
OUTPUT_PRICE_PER_MILLION=1.20

REQUESTS_PER_DAY=2000
AVG_INPUT_TOKENS=1200
AVG_OUTPUT_TOKENS=300
PEAK_REQUESTS_PER_MINUTE=30

RPM_LIMIT=60
TPM_LIMIT=100000

MONTHLY_BUDGET_USD=50
DAILY_BUDGET_USD=2
SAFETY_MARGIN_PERCENT=20

## 6. Implementation Steps

1. Load configuration values from the .env file.
2. Create the FeatureBudget class.
3. Calculate daily input tokens.
4. Calculate daily output tokens.
5. Calculate total daily token consumption.
6. Estimate daily and monthly API costs.
7. Calculate peak RPM and TPM with a safety margin.
8. Check RPM and TPM limits.
9. Check daily and monthly budget constraints.
10. Display PASS or REVIEW results.
11. Create unit tests to verify calculations.

## 7. Execution

Run the budget application:

python budget.py

Run unit tests:

python -m unittest -v test_budget

## 8. Sample Input

Requests per day: 2000

Average input tokens: 1200

Average output tokens: 300

Peak requests per minute: 30

Daily budget: $2

Monthly budget: $50

## 9. Expected Output

The program displays a TOKEN ECONOMICS REPORT containing:

- Input tokens per day
- Output tokens per day
- Total tokens per day
- Estimated daily cost
- Estimated monthly cost
- Peak RPM with safety margin
- Peak TPM with safety margin

It also displays:

CHECKS

RPM capacity: PASS / REVIEW

TPM capacity: PASS / REVIEW

Daily budget: PASS / REVIEW

Monthly budget: PASS / REVIEW

Unit tests verify cost calculations and limit checking.

## 10. Result

Successfully developed a Token Economics and Budgeting application using Python to estimate token consumption, calculate API costs, evaluate rate limits, and verify daily and monthly budget constraints.
