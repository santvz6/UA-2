import os
import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from db import create_db_and_tables, drop_db_and_tables, seed_users
from api import movies, users



# Create logs folder if it doesn't exist
os.makedirs('logs', exist_ok=True)

logging.basicConfig(level=logging.INFO, filename='logs/movies.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Creating db tables")
    drop_db_and_tables()
    create_db_and_tables()
    logging.info("Seeding users")
    seed_users()
    logging.info("Application started")
    yield
    logging.info("Application shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(movies.router)
app.include_router(users.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
