# AI Resume Critiquer

AI-powered ATS Resume Analyzer built using Streamlit and Groq LLM APIs.

## Features

- ATS Resume Score
- Resume Analysis
- Missing Keywords Detection
- Technical Skills Evaluation
- Project Analysis
- AI-generated Interview Questions
- Resume Rewriting Suggestions
- Job Description Matching

---

## Tech Stack

- Python
- Streamlit
- Groq API
- PyPDF2
- dotenv

---

## Project Architecture

```text
User Resume
     ↓
PDF Parser
     ↓
Text Extraction
     ↓
Groq LLM Analysis
     ↓
ATS Feedback + Suggestions
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shanjaiy2006/AI-Resume-Critiquer.git
```

### Navigate to Project

```bash
cd AI-Resume-Critiquer
```

### Install Dependencies

```bash
uv sync
```

### Add Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## Screenshots

(Add project screenshots here)

---

## Future Improvements

- Resume Rewrite Engine
- Dynamic ATS Score Extraction
- PDF Feedback Report
- Multi-Resume Comparison
- RAG-based Resume Intelligence
- Authentication System

---

## Author

Shanjaiy Samarjith

- GitHub: https://github.com/shanjaiy2006
- LinkedIn: https://www.linkedin.com/in/shanjaiysamarjithgs
