from fastapi import FastAPI 
import uvicorn
from utils import summarize_website
from typing import Optional, List
from pydantic import BaseModel

api = FastAPI()

class SumryInput(BaseModel):
    url:str 
    num_sentences:int 
    bonus_words:Optional[List]

@api.get("/")
def home():
    return {"message": "Welcome to websumry"}


@api.post("/summary")
def get_summry(input: SumryInput):
    result = summarize_website(url=input.url, num_sentences=input.num_sentences, bonus_words=input.bonus_words)
    return result 

if "__name__"== "__main___":
    uvicorn.run(api)