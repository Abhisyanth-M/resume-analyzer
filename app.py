import streamlit as st
import pdfplumber
import re

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("RESUME ANALYZER")

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
job_desc = st.text_area("Paste the job description here")

if uploaded_file is not None:
    text = ""

    # Extract text
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    text_lower = text.lower()

    # Show resume
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", text, height=300)

    # 🔥 Resume Detection
    resume_keywords = [
        "education", "skills", "projects", "experience",
        "summary", "objective", "internship", "profile"
    ]

    if any(word in text_lower for word in resume_keywords):
        st.success("This looks like a resume")
    else:
        st.error("This may not be a resume")

    # 🔥 Contact Detection
    email_found = re.search(r"\S+@\S+", text)
    phone_found = re.search(r"\d{10}", text)

    if email_found:
        st.success(f"Email: {email_found.group()}")
    if phone_found:
        st.success(f"Phone: {phone_found.group()}")

    # 🔥 Skill Extraction
    st.subheader("Detected Skills")

    skills_list = [
        "python", "java", "c++", "sql", "mysql",
        "machine learning", "deep learning", "nlp",
        "data science", "pandas", "numpy", "matplotlib",
        "scikit-learn", "tensorflow", "keras",
        "power bi", "excel", "tableau",
        "fastapi", "streamlit", "flask", "django",
        "docker", "git", "github"
    ]

    found_skills = [skill for skill in skills_list if skill in text_lower]

    if found_skills:
        st.write(found_skills)
    else:
        st.write("No major skills detected")

    # 🔥 JOB MATCHER
    if job_desc:
        st.subheader("Job Match Analysis")

        job_desc_lower = job_desc.lower()

        resume_words = set(text_lower.split())
        job_words = set(job_desc_lower.split())

        matched_words = resume_words.intersection(job_words)

        if len(job_words) > 0:
            match_percent = (len(matched_words) / len(job_words)) * 100
        else:
            match_percent = 0

        st.write(f"Match Score: {round(match_percent, 2)}%")

        missing_words = job_words - resume_words

        st.subheader("Missing Keywords")
        st.write(list(missing_words)[:20])

    # 🔥 SMART SUGGESTIONS (NO AI NEEDED)
    st.subheader("Suggestions")

    recommendations = {
        "python": ["Learn advanced Python", "Practice DSA"],
        "machine learning": ["Build ML projects", "Learn model evaluation"],
        "sql": ["Practice joins", "Learn optimization"],
        "streamlit": ["Deploy app", "Improve UI"],
        "data science": ["Work on datasets", "Improve visualization"],
        "github": ["Add README", "Showcase projects"]
    }

    suggestions = []

    for skill in found_skills:
        if skill in recommendations:
            suggestions.extend(recommendations[skill])

    if suggestions:
        for s in set(suggestions):
            st.write(f"- {s}")
    else:
        st.write("Add more skills to get suggestions")
