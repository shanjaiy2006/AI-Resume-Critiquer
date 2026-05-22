import streamlit as st
from PyPDF2 import PdfReader
import io
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")
st.title("AI Resume Critiquer")
st.write(
    "Upload your resume in PDF format, and get AI-powered feedback tailored to your job application goals."
)

st.markdown(
    """
<style>
.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}
</style>
""",
    unsafe_allow_html=True,
)


uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_description = st.text_area(
    "Enter the job description or role you're targeting", height=150
)
analyze_button = st.button("Analyze Resume")
rewrite_button = st.button("Rewrite Resume")


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_text_from_file(uploded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


if analyze_button and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file is empty. Please upload a valid resume.")
            st.stop()

        if not job_description.strip():
            st.error("Please enter a job description to analyze against.")
            st.stop()

        # Resume Preview
        with st.expander("View Extracted Resume Text"):
            st.text(file_content)

        # AI Prompt
        prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume and provide:

# ATS Score
Give ATS score out of 100.

# Resume Strengths

# Weaknesses

# Missing Keywords
Return the missing keywords separately in comma-separated format.

# Improvements Needed

# Technical Skills Analysis

# Project Analysis

# Interview Questions From Resume
Generate likely interview questions based on this resume and job description.

# Final Verdict

Job Description:
{job_description}

Resume:
{file_content}

Return the response in proper markdown format with headings and bullet points.
"""

        # Loading Spinner
        with st.spinner("Analyzing your resume..."):

            client = Groq(api_key=GROQ_API_KEY)

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1000,
            )

            feedback = response.choices[0].message.content

        # Temporary ATS Score
        ats_score = 85

        # Success Message
        st.success("Resume analyzed successfully!")

        # ATS Section
        st.subheader("ATS Score")

        st.progress(ats_score / 100)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("ATS Score", f"{ats_score}%")

        with col2:
            st.metric("Missing Keywords", "6")

        # Missing Keywords Warning
        st.warning("Missing Keywords: React, Docker, AWS")

        # Feedback Section
        st.subheader("AI Feedback on Your Resume")

        st.markdown(feedback)

        # Download Report
        st.download_button(
            label="Download Feedback Report",
            data=feedback,
            file_name="resume_feedback.txt",
            mime="text/plain",
        )

    except Exception as e:

        st.error(f"An error occurred: {str(e)}")
