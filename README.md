# 🔍 Resume-Based AI Job Matcher using OpenAI Embeddings & Similarity Search

This project is an intelligent job recommendation system powered by **semantic similarity search** using **OpenAI embeddings**. Users upload their CV (resume), and the platform instantly finds the most relevant job descriptions by comparing vector representations of the resume and jobs.

> It demonstrates the power of LLM-based embeddings and cosine similarity to solve a real-world NLP problem: **matching a person to the right job**.

---

## 🖼️ Preview

| Resume Upload + Filtering | Matching Jobs with Scores |
|---------------------------|----------------------------|
| ![Upload Resume](./screenshots/upload.png) | ![Results Page](./screenshots/results.png) |

> 📌 Place your images inside a `/screenshots` folder in the root directory, and rename accordingly.

---

## 🎯 Project Objectives

- 🔎 **Match resumes to job offers using semantic similarity** (not just keyword matching).
- ⚡ Quickly identify strong, moderate, or weak matches using scoring.
- 📂 Help candidates and recruiters streamline the job search and hiring process.
- 🧠 Apply real-world **NLP, embeddings, and similarity search** concepts using OpenAI models.

---

## 🔑 Key Features

- 📄 Upload CVs (`.pdf` or `.docx`) and parse content using Python libraries.
- 🔁 Generate vector embeddings of resumes and job descriptions via **OpenAI's text-embedding-ada-002**.
- 📏 Compute **cosine similarity** to determine job fit.
- 📍 Optional filters: **job title**, **location**, and **type** (on-site/hybrid).
- ✅ Display strong/moderate/weak matches with clear scoring and job cards.
- ➕ Add new job listings dynamically via admin panel.

---

## 💡 Technical Concepts

| Concept | Description |
|--------|-------------|
| ✅ **OpenAI Embeddings** | Turns resumes and job descriptions into numerical vectors |
| ✅ **Cosine Similarity** | Computes semantic relevance between two vectors |
| ✅ **FastAPI** | Handles file upload, job CRUD, and match scoring |
| ✅ **React SPA** | Provides dynamic, modern frontend interface |
| ✅ **Vector Search** | Enables accurate job-to-resume semantic comparison |
| ✅ **Text Parsing** | Extracts raw content from `.pdf` and `.docx` resumes |

---

## 🧰 Tech Stack

### 🖥️ Frontend:
- React, JSX, CSS Grid
- File Input + Resume Filters
- Dynamic Job Cards with Match Levels

### ⚙️ Backend:
- FastAPI (Python)
- OpenAI API for Embeddings
- Pandas, NumPy, Scikit-learn
- Resume Parsing: PyMuPDF (PDF), python-docx

