from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .services.db_handler import table_init


app = FastAPI()
app.include_router(router)


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    #"link to main site URL",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def main():
    table_init()

@app.get("/")
async def home():
    return {"message":"API is up and running"}