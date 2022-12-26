from fastapi import FastAPI, HTTPException
import uvicorn
from utils import summarize_website
from typing import Optional, List
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Home",
        "description": "Return welcome message",
    },
    {
        "name": "Summary",
        "description": "Takes an url, number of sentences and an optional bonus words as input and returns a summary",
    },
    
]

api = FastAPI(openapi_tags=tags_metadata, title="Websumry - summarize a website anytime!")

class SumryInput(BaseModel):
    url: str 
    num_sentences: int 
    bonus_words: Optional[List] = ["important"]

@api.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to websumry"}


@api.post("/summary", tags=["Summary"])
def get_summry(input: SumryInput):
    if input:
        result = summarize_website(url=input.url, num_sentences=input.num_sentences, bonus_words=input.bonus_words)
        return {"summary": result }
    else:
        raise HTTPException(status_code=500, detail="Please provide the necessary inputs") 

if "__name__"== "__main___":
    uvicorn.run(api)