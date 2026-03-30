import streamlit as st
import pdfplumber

st.title("RESUME ANALYZER")
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
job_desc=st.text_area("Paste the job description here")

if uploaded_file is not None:
    text = ""

    # Extract text
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    # Show resume
    st.write("Extracted Resume Text")
    st.text_area("Resume Content", text, height=400)

    text_lower = text.lower()

    # 🔥 Resume detection (optional)
    resume_keywords = [
        "education", "skills", "projects", "experience",
        "summary", "objective", "internship"
    ]

    if any(word in text_lower for word in resume_keywords):
        st.success("✅ This looks like a resume")
    else:
        st.error("❌ This may not be a resume")

    # 🔥 JOB MATCHER
    if job_desc:
        st.write("### 🎯 Job Match Analysis")

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

        st.write("### ❌ Missing Keywords")
        st.write(list(missing_words)[:20])

    
    resume_keywords = [
        "education",
        "skills",
        "projects",
        "experience",
        "summary",
        "objective",
        "internship",
        "profile"
    ]

    if any(word in text_lower for word in resume_keywords):
        st.success("✅ This looks like a resume")
    else:
        st.error("❌ This may not be a resume. Please upload a valid resume.")

    # 🔽 Optional: detect contact details
    import re

    email_found = re.search(r"\S+@\S+", text)
    phone_found = re.search(r"\d{10}", text)

    if email_found and phone_found:
        st.success("📞 Contact details detected")

    # 🔽 Skill Extraction
    skills_list = [
    "python", "java", "c++", "sql", "mysql",
    "machine learning", "deep learning", "nlp",
    "data science", "pandas", "numpy", "matplotlib",
    "scikit-learn", "tensorflow", "keras",
    "power bi", "excel", "tableau",
    "fastapi", "streamlit", "flask", "django",
    "docker", "git", "github"
   ]

    found_skills = []

    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)

    st.write("### Detected Skills")

    if found_skills:
        st.success(", ".join(found_skills))
    else:
        st.warning("No major skills detected")

    # 🎯 Resume Score
    score = 0

# Keywords scoring
    important_keywords = [
    "python", "machine learning", "data science",
    "projects", "github", "internship"
    ]

    for word in important_keywords:
        if word in text_lower:
           score += 10

# Contact info scoring
    if "@" in text:
        score += 10

    if any(char.isdigit() for char in text):
        score += 10

# Limit score
    score = min(score, 100)

    st.write("### 📊 Resume Score")
    st.progress(score)
    st.write(f"Score: {score}/100")

    st.write("Suggestions:")

    if "project" not in text_lower:
        st.warning("Add projects to your resume")

    if "skill" not in text_lower:
        st.warning("Mention your technical skills clearly")

    if "internship" not in text_lower:
        st.warning("Try adding internship experience")

    if "github" not in text_lower:
        st.warning("Add your GitHub profile")

    if score > 70:
        st.success("Great resume! You're on the right track!")