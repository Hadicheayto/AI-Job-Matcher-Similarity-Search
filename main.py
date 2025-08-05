from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import extract_text_from_cv, embed_text, load_jobs, calculate_similarity, add_job_to_db
import pandas as pd
from fastapi import UploadFile, Form


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Search Job with AI API"}

@app.post("/match")
async def match_jobs(
    cv: UploadFile,
    job_title: str = Form(""),
    location: str = Form(""),
    job_type: str = Form("")
):
    try:
        text = extract_text_from_cv(cv)
        if not text:
            return {"error": "CV could not be parsed"}

        # Combine CV with user inputs for better embedding context
        combined_text = f"{job_title} {location} {job_type} {text}"

        # Embed the combined input
        cv_emb = embed_text(combined_text)
        jobs = load_jobs()

        if jobs.empty:
            return {"matches": []}

        jobs["score"] = jobs["embedding"].apply(lambda e: calculate_similarity(cv_emb, e) * 100)
        jobs = jobs.sort_values(by="score", ascending=False)

        all_matches = jobs[["title", "description", "location", "job_type", "skills", "score"]].to_dict(orient="records")
        return {"matches": all_matches}

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": "Internal server error"}
    

class JobRequest(BaseModel):
    title: str
    description: str
    location: str
    job_type: str
    skills: str

@app.post("/add-job")
async def add_job(job: JobRequest):
    try:
        add_job_to_db(job.title, job.description, job.location, job.job_type, job.skills)
        return {"message": "Job added successfully"}
    except Exception as e:
        print("❌ ERROR ADDING JOB:", str(e))
        return {"error": "Failed to add job"}

@app.get("/jobs")
def get_jobs():
    try:
        jobs = load_jobs()
        return {"jobs": jobs[["title", "description", "location", "job_type", "skills"]].to_dict(orient="records")}
    except Exception as e:
        print("❌ ERROR LOADING JOBS:", str(e))
        return {"error": "Failed to load jobs"}
