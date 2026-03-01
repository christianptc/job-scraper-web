from fastapi import APIRouter, status, Response

from .services import db_handler
from .services import scraper

db = db_handler.handler()
router = APIRouter()

@router.get("/users/{user_id}/{table}/jobs")
async def fetch_stored_jobs(user_id: str, table: str):
    
    job_ids = db.get_stored_jobIDs(user_id, table)

    if not job_ids:
        return []
    
    jobs = db.get_jobs_byID(job_ids)

    stored_jobs = []
    for job in jobs:
        id, company, jobtitle, location, link, date = job
        stored_jobs.append({
            "id":id,
            "company":company,
            "job_title":jobtitle,
            "location":location,
            "link":link,
            "date":date
        })

    return stored_jobs

@router.post("/users/{user_id}/activity", status_code=status.HTTP_204_NO_CONTENT)
async def log_activity(user_id: str):
    

    return Response(status_code=status.HTTP_204_NO_CONTENT)

