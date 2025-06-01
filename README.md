# AI-Powered Code Review System - README

## Overview

This project is an AI-powered code review system that automatically analyzes code snippets and suggests improvements. Built with React for the frontend, FastAPI for the backend, Google Gemini AI for code analysis, and PostgreSQL for data storage.

## Features

- AI-powered code analysis using Google Gemini
- Automatic code improvement suggestions
- Historical code review tracking
- User-friendly interface
- Secure API endpoints
- Database storage of all code reviews

## Technology Stack

| Component      | Technology       |
| -------------- | ---------------- |
| **Frontend**   | React            |
| **Backend**    | FastAPI (Python) |
| **AI Engine**  | Google Gemini    |
| **Database**   | PostgreSQL       |
| **API Client** | Axios            |
| **ORM**        | SQLAlchemy       |

## Project Structure

```
code-review-system/
├── backend/             # FastAPI server
│   ├── venv/            # Python virtual environment
│   ├── .env             # Environment variables
│   ├── main.py          # Main backend code
│   └── requirements.txt # Python dependencies
├── frontend/            # React application
│   ├── public/
│   ├── src/
│   │   ├── App.js       # Main frontend component
│   │   └── ...          # Other React files
│   ├── package.json     # Frontend dependencies
│   └── ...
└── README.md            # This file
```

## System Components

### 1. Frontend (React)

- **Location**: `/frontend`
- **Purpose**: User interface for submitting code and displaying feedback
- **Key Files**:
  - `App.js`: Main component with form and feedback display
  - `package.json`: Lists all frontend dependencies

### 2. Backend (FastAPI)

- **Location**: `/backend`
- **Purpose**: Processes requests, communicates with Gemini AI, and interacts with database
- **Key Files**:
  - `main.py`: Contains all API endpoints and database logic
  - `.env`: Stores sensitive information (API keys, database credentials)

### 3. Database (PostgreSQL)

- **Purpose**: Stores all submitted code snippets and AI feedback
- **Tables**:
  - `code_snippets`: Stores submitted code
  - `reviews`: Stores AI feedback linked to code snippets

### 4. AI Engine (Google Gemini)

- **Integration**: Called through Google's API
- **Model**: `gemini-1.5-flash`
- **Function**: Analyzes code and generates improvement suggestions

## Setup Instructions

### Prerequisites

1. Python 3.7+
2. Node.js 14+
3. PostgreSQL
4. Google Gemini API key

### Step-by-Step Installation

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
```

#### 2. Set up the Backend

```bash
cd backend
python -m venv venv       # Create virtual environment

# Activate environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt  # Install dependencies
```

#### 3. Configure Environment Variables

Create `.env` file in `/backend`:

```env
DATABASE_URL=postgresql://username:password@localhost/code_review_db
GEMINI_API_KEY=your_gemini_api_key
```

#### 4. Set up the Frontend

```bash
cd ../frontend
npm install  # Install dependencies
```

#### 5. Set up PostgreSQL Database

1. Create a new database named `code_review_db`
2. The tables will be automatically created when you run the backend

## Running the Application

### 1. Start the Backend

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

### 2. Start the Frontend

```bash
cd ../frontend
npm start
```

The application will open in your browser at: [http://localhost:3000](http://localhost:3000)

### 3. Using the Application

1. Paste your code in the text area
2. Click "Get Feedback"
3. View the AI-generated suggestions

## API Endpoints

| Endpoint  | Method | Description            | Request Body                 |
| --------- | ------ | ---------------------- | ---------------------------- |
| `/review` | POST   | Submit code for review | `{"code": "your code here"}` |

## Testing the API

You can test the API using curl:

```bash
curl -X POST "http://localhost:8000/review" \
-H "Content-Type: application/json" \
-d '{"code": "def add(a, b): return a + b"}'
```

## Database Schema

```sql
CREATE TABLE code_snippets (
    id SERIAL PRIMARY KEY,
    code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    snippet_id INTEGER REFERENCES code_snippets(id),
    feedback TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## How It Works

1. User submits code through React frontend
2. Frontend sends code to FastAPI backend
3. Backend saves code to PostgreSQL database
4. Backend sends code to Google Gemini for analysis
5. Gemini returns feedback
6. Backend saves feedback to database
7. Backend returns feedback to frontend
8. Frontend displays feedback to user

## Troubleshooting

1. **CORS Errors**: Ensure CORS middleware is properly configured in `main.py`
2. **Database Connection Issues**: Verify `.env` file has correct database credentials
3. **Gemini API Errors**: Check your API key and billing status
4. **Module Not Found**: Ensure you've installed all dependencies and activated virtual environment

## Future Improvements

- [ ] User authentication system
- [ ] Code quality scoring
- [ ] Support for multiple programming languages
- [ ] Integration with GitHub/GitLab
- [ ] Historical comparison of code changes
- [ ] Email notifications for reviews
- [ ] Team collaboration features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google Gemini for AI capabilities
- FastAPI and React communities
- SQLAlchemy for ORM support
