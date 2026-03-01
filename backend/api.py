from fastapi import APIRouter

from .services import db_handler
from .services import scraper

db = db_handler.handler()
router = APIRouter()

@router.get("/init/{user_id}/{table}")
async def initialize_user_data(user_id: str, table: str):
    
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

