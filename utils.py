from dotenv import load_dotenv
import pandas as pd
import numpy as np
from openai import OpenAI
from PyPDF2 import PdfReader
import docx
from io import BytesIO
from sklearn.metrics.pairwise import cosine_similarity
import os
import ast


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DB = "jobs.csv"

def extract_text_from_cv(file):
    try:
        contents = file.file.read()
        if file.filename.endswith(".pdf"):
            reader = PdfReader(BytesIO(contents))
            return " ".join(page.extract_text() or "" for page in reader.pages).strip()
        elif file.filename.endswith(".docx"):
            doc = docx.Document(BytesIO(contents))
            return " ".join(p.text for p in doc.paragraphs).strip()
    except:
        return None

def embed_text(text):
    response = client.embeddings.create(input=[text], model="text-embedding-3-small")
    return response.data[0].embedding

def calculate_similarity(e1, e2):
    return float(cosine_similarity([e1], [e2])[0][0])

def add_job_to_db(title, description, location, job_type, skills):
    full_text = f"{title} {location} {job_type} {description} {skills}"
    embedding = embed_text(full_text)

    new_row = pd.DataFrame([{
        "title": title,
        "description": description,
        "location": location,
        "job_type": job_type,
        "skills": skills,
        "embedding": embedding
    }])

    if os.path.exists(DB):
        df = pd.read_csv(DB)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(DB, index=False)


def load_jobs():
    if not os.path.exists(DB):
        return pd.DataFrame(columns=["title", "description", "location", "job_type", "skills", "embedding"])
    df = pd.read_csv(DB)
    df["embedding"] = df["embedding"].apply(ast.literal_eval)
    return df