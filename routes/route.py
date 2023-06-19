from fastapi import APIRouter
from models.todo import TodoBase
from schema.schemas import list_serial
from config.database import collection_name
from bson import ObjectId


router = APIRouter()


# Get all todos

@router.get("/")

async def get_todo_base():
    todo = list_serial(collection_name.find())
    return todo


# Post a todo

@router.post("/")

async def post_todo_base(todo_base: TodoBase):

    collection_name.insert_one(todo_base.dict())

    return {"message": "Todo created successfully"}

#put todo
@router.put("/{id}")
async def put_todo_base(id:str,todo_base:TodoBase):
    collection_name.find_one_and_update({"_id":ObjectId(id)}, {"$set":todo_base.dict()})

#delete todo
@router.delete("/{id}")
async def delete_todo_base(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})

