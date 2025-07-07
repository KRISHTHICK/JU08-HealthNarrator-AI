# app.py – HealthNarrator AI: Medical Report Explainer

import streamlit as st
import fitz  # PyMuPDF
import ollama
import re

# --- Step 1: Extract text from PDF ---
def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = "\n".join(page.get_text() for page in doc)
    return text

# --- Step 2: Pre-clean text ---
def clean_report_text(text):
    return re.sub(r"\s+", " ", text).strip()

# --- Step 3: Build LLM prompt ---
def generate_prompt(text, language="English"):
    prompt = f"""
You are a health assistant. Read this medical report and explain it in simple, layman-friendly terms.
Return the following:
1. Key Findings (Test name: value + remark)
2. Layman Summary (bullet points)
3. 3–5 Questions the patient should ask their doctor
4. Translate summary to {language}

Medical Report:
{text[:3000]}
"""
    return prompt

# --- Step 4: Use LLaMA to summarize ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="HealthNarrator AI", layout="wide")
st.title("🧠 HealthNarrator AI – Medical Report Explainer")

uploaded_file = st.file_uploader("Upload Medical Report (PDF)", type=["pdf"])
language = st.selectbox("Choose output language", ["English", "Hindi", "Bengali", "Tamil", "Telugu"])

if uploaded_file:
    with st.spinner("Extracting and processing the medical report..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_report_text(raw_text)
        st.success("✅ Text extracted.")

    if st.button("🧠 Generate Explanation"):
        with st.spinner("Generating explanation with LLM..."):
            prompt = generate_prompt(cleaned_text, language)
            result = query_llm(prompt)
            st.markdown("### 📋 Explained Medical Report")
            st.markdown(result)
else:
    st.info("Please upload a PDF medical report to begin.")
