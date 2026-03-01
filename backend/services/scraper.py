import requests
# from db_handler import ...

def get_jobs_raw(search, ort, umkreis, amount):
    url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"
    headers = {"X-API-Key": "jobboerse-jobsuche"}

    params = {
        "was": f"{search}",
        "wo": f"{ort}",
        "umkreis": {umkreis},
        "page": 1,
        "size": {amount},
        "sortierung" : "datum"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()
    raw_jobs = data.get('stellenangebote', [])

    total_new_jobs = 0
    for job in raw_jobs:
        ref_nr = job.get('refnr', None)
        company_name = job.get('arbeitgeber', None)
        position = job.get('titel', job.get('beruf', None))
        location = job.get('arbeitsort', {}).get('ort', None)
        link = job.get('externeUrl', f"https://www.arbeitsagentur.de/jobsuche/jobdetail/{ref_nr}")
        date_posted = job.get('aktuelleVeroeffentlichungsdatum', None)
        
        # check = db_handler.scrape_internship(company_name, position, location, link, date_posted)
        # if check:
        #     total_new_jobs += 1

    # return len(raw_jobs), total_new_jobs
    return