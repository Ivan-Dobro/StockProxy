from fastapi import FastAPI
from . import models,schemas
from .database import engine,SessionLocal
from sqlalchemy.orm import  Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return {"data":
            {'name':'Hi Stock!'}
            }
