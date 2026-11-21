
# WEEK 3 – Gemini API Monitoring using MongoDB Atlas

## Aim

To develop a Gemini API monitoring application using Python that tracks API usage, measures response latency, estimates token costs, and stores API usage logs in MongoDB Atlas.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- MongoDB Atlas
- PyMongo
- Pandas
- Matplotlib
- Environment Variables (`.env`)

## Tools Used

- Python
- Visual Studio Code
- Gemini API
- MongoDB Atlas
- MongoDB Compass (optional)

## Folder Structure

```text
WEEK3/
├── main.py
├── check_models.py
├── test_mongodb.py
├── view_logs.py
├── requirements.txt
├── .env
├── .env.example
└── README.md
```

## Installation Steps

1. Install Python on your system.

2. Open the WEEK3 folder in VS Code.

3. Create a virtual environment:

```bash
python -m venv myenv
```

4. Activate the virtual environment:

```bash
myenv\Scripts\activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file and add your Gemini API key and MongoDB Atlas connection string:

```text
GEMINI_API_KEY=your_api_key_here
MONGODB_URI=your_mongodb_connection_string
GEMINI_MODEL=gemini-2.5-flash
```

7. Create a MongoDB Atlas account and configure your database connection.

**Note:** Never upload your actual API key or MongoDB connection string to GitHub.

## Execution Steps

**Step 1: Check Available Gemini Models**

Run the following command:

```bash
python check_models.py
```

**Step 2: Test MongoDB Connection**

```bash
python test_mongodb.py
```

1. The program connects to MongoDB Atlas.
2. It checks the database connection.
3. It inserts a test document.
4. A success message is displayed.

**Step 3: Run the Main Application**

```bash
python main.py
```

1. The program connects to the Gemini API.
2. Enter a prompt or question.
3. Gemini generates an AI response.
4. The application records token usage.
5. Response latency and estimated cost are calculated.
6. API monitoring details are stored in MongoDB Atlas.

**Step 4: View API Usage Logs**

```bash
python view_logs.py
```

1. The program retrieves stored API usage logs.
2. It displays token consumption and response latency.
3. It displays estimated API costs.
4. It generates a usage chart.

## Expected Output

The application displays Gemini responses and stores API monitoring details in MongoDB Atlas.

**Example:**

```text
Connecting to MongoDB Atlas...
MongoDB Connected Successfully!

Database: GenAI_Monitoring
Collection: api_usage_logs

Inserted ID: <generated document ID>
```

The log viewer displays API usage information and generates a chart showing monitoring details.

## Result

Successfully developed a Gemini API monitoring application using Python and MongoDB Atlas to track token usage, response latency, estimated API costs, and store API usage logs.
