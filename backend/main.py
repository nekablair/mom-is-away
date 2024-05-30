from fastapi import FastAPI
from backend.models import Todo

app = FastAPI()

#Swagger is built in: http://127.0.0.1:8000/docs


#with FastAPI, async is built in, uses asgi, which is async

@app.get("/")
async def root():
    return {"message": "Welcome to the Mom Is Away App"}

todos = []

#get all todos

@app.get("/all/")
async def get_todos():
    return {"todos": todos}


#get single todo

@app.get("/a_todo/{todo_id}/")
async def get_a_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo_id": todo_id}
        return {"message": "No todos found"}


#create a todo

@app.post("/todos/")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added" }


#update a todo

@app.put("/todos/{todo_id}/")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"message": "Todo has been updated"}
        return {"message": "No todos found to update"}


#delete a todo

@app.delete("/a_todo/{todo_id}/")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo item has been deleted"}
        return {"message": "No todos found"}
    