# JU08-HealthNarrator-AI
GenAI

🧠 HealthNarrator AI – Medical Report Explainer for Patients
💡 What It Does
HealthNarrator AI helps patients understand complex medical reports by:

Accepting medical documents (lab reports, prescriptions, discharge summaries)

Extracting relevant medical terms, test values, and diagnoses

Explaining each section in layman's terms

Highlighting critical findings and next steps

Supporting multilingual output (e.g., English + Hindi)

⚙️ Key Features
Feature	Description
📤 Upload Medical Report	Accepts PDF or image format
🧬 Extract Health Terms	Detects values like Hemoglobin, Creatinine, etc.
💬 Simple Explanation	Converts medical jargon into patient-friendly text
🩺 Risk Alerts	Flags abnormal or risky values (e.g., high sugar)
🌐 Multilingual Support	Explains report in English + selected language
📝 Doctor Questions Generator	Creates 3–5 questions patients can ask doctors

🏥 Ideal Use Cases
Patients confused by lab reports or health records

Family members assisting with elderly care

NGOs or rural health workers explaining reports in regional languages

Healthcare apps offering smart reports

🧱 Tech Stack
Component	Tool
UI	Streamlit
OCR (if needed)	Tesseract / Azure Vision
Text Extraction	PyMuPDF / pdfplumber
Medical Parsing	Custom rules + LLM (Ollama / GPT)
Language Model	Ollama (TinyLLaMA / LLaMA3), Azure GPT, or Claude
Translation	Azure Translator API or Google Translate API

# 🧠 HealthNarrator AI – Medical Report Explainer

HealthNarrator AI is an intelligent assistant that simplifies medical reports using LLMs. It translates medical jargon into plain language, flags important findings, and suggests questions patients can ask their doctor.

---

## 🔧 Features

- Upload medical reports in PDF format
- Extract and clean raw text from reports
- Summarize in layman-friendly language
- Highlight test results and remarks
- Suggest questions for patient–doctor discussion
- Multilingual support (e.g., English, Hindi, Tamil)

---

## 🚀 Setup

```bash
git clone https://github.com/yourusername/healthnarrator-ai.git
cd healthnarrator-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
