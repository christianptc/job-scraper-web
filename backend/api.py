from fastapi import APIRouter

router = APIRouter()

@router.get("/init/{user_id}/{table}")
async def initialize_user_data(user_id: str, table: str):
    
    stored_jobs = jobs_from_db = [
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "1", "company": "Google", "position": "Junior Softwareentwickler"},
        {"ID": "2", "company": "Google", "position": "Werkstudent"}
    ]

    return stored_jobs