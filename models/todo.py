from pydantic import BaseModel

class TodoBase(BaseModel):
    name: str
    description: str 
    completed: bool