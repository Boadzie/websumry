from fastapi import FastAPI 
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
    url:str 
    num_sentences:int 
    bonus_words:Optional[List]

@api.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to websumry"}


@api.post("/summary", tags=["Summary"])
def get_summry(input: SumryInput):
    result = summarize_website(url=input.url, num_sentences=input.num_sentences, bonus_words=input.bonus_words)
    return {"summary": result }

if "__name__"== "__main___":
    uvicorn.run(api)