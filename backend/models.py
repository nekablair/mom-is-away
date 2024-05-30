from fastapi import FastAPI
from pydantic import BaseModel

#validation is built in
class Todo(BaseModel):
    id: int
    item: str 