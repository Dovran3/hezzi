from fastapi import FastAPI
from router import book_app

app = FastAPI()

app.include_router(book_app, prefix='/books')
