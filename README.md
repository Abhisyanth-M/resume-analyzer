# AI Resume Analyzer with Job Matching

A Streamlit web application that analyses a PDF resume against a job description and provides a match score, missing skills and improvement suggestions.

## Live Demo
https://resume-analyzer-c34qtzutcpbgaxwkjk6udk.streamlit.app/

## Overview
AI Resume Analyzer helps job seekers understand how well their resume matches a specific job description. Upload your resume and paste the job description — the app instantly shows your match percentage, missing skills and what to improve.

## Features
- Upload PDF resume
- Extract text from resume using pdfplumber
- Detect if uploaded file is a valid resume
- Extract key technical skills from resume
- Paste any job description
- Calculate job match percentage
- Show missing skills not found in resume
- Provide improvement suggestions

## Tech Stack
- Python
- Streamlit
- pdfplumber

## How It Works
1. User uploads a PDF resume
2. pdfplumber extracts the text from the PDF
3. App scans the text and identifies technical skills
4. User pastes a job description
5. App compares resume skills with job description requirements
6. Match percentage, missing skills and suggestions are displayed

## Installation and Running Locally
```bash
git clone https://github.com/Abhisyanth-M/resume-analyzer
cd resume-analyzer
pip install streamlit pdfplumber
python -m streamlit run app.py
```

## Limitations
- Skill detection is based on keyword matching — may miss contextual skills
- Only supports PDF format
- Match percentage is approximate and based on keyword overlap
- Does not analyse resume formatting or structure

## Future Improvements
- Support for Word document uploads
- NLP-based skill extraction for better accuracy
- Resume scoring based on formatting and structure
- Suggestions for resume rewriting based on job description
- Support for multiple job descriptions comparison

## GitHub
https://github.com/Abhisyanth-M/resume-analyzer
```
