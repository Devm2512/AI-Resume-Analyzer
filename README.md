# 🧠 AI Resume Analyzer & Job Description Matcher

An AI-powered intelligent system that automates resume screening by matching candidate resumes with job descriptions using NLP, Machine Learning, and LLM-based skill extraction.

This project helps HR teams and recruiters quickly identify the most relevant candidates by generating an **AI-driven compatibility score** between resumes and job descriptions.

---

## 🚀 Key Features

- 📄 **PDF Resume Parsing** using PyPDF2
- 🧹 **Text Cleaning & Preprocessing Pipeline**
- 🧠 **LLM-based JD Parsing (Flan-T5)**
  - Extracts structured skills automatically
- 📊 **Skill Categorization**
  - Must Have
  - Intermediate
  - Good to Have
- 🎯 **Resume vs JD Matching Engine**
- 📉 **Weighted Scoring System**
- ⚙️ Modular and scalable architecture

---

## 🧠 Problem Statement

Recruiters often face challenges such as:
- Time-consuming manual resume screening
- Inconsistent candidate evaluation
- Difficulty extracting structured skills from job descriptions
- Bias in initial screening

👉 This system automates the entire initial screening process using AI.

---


---

## ⚙️ Tech Stack

- Python 🐍
- NLP (NLTK, Regex)
- Machine Learning (Scikit-learn)
- Transformers (Hugging Face - Flan-T5)
- PyPDF2
- JSON Processing

---

## 📊 Scoring Logic

| Skill Type       | Weight |
|-----------------|--------|
| Must Have        | 50%    |
| Intermediate     | 30%    |
| Good to Have     | 20%    |

👉 Final Score = Weighted Match Percentage

---

## 🔄 Workflow

1. Upload Resume (PDF)
2. Extract and clean text from resume
3. Input Job Description
4. LLM extracts structured skills
5. Resume skills are matched with JD skills
6. Weighted scoring is applied
7. Final recommendation is generated

---

## 📦 Installation

```bash
git clone <your-repo-link>
cd AI-Resume-Analyzer
pip install -r requirements.txt
