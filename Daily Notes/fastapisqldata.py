# pip install sqlalchemy psycopg2

from sqlalchemy import create_engine, text

Host = "postgresql+psycopg2://username:password@ep-white-rain-379558-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(Host, pool_pre_ping=True)
conn = engine.connect()

result = conn.execute(text("SELECT * FROM users;"))
for row in result:
    # print(row)
    pass

# conn.commit() # use this only while update or create a rows or table
conn.close()

import pandas as pd
df = pd.read_sql("SELECT * FROM users;", engine)
# print(df)

engine.dispose()

# ---------------------------------------------------------------------------
# FastAPI app: GET /users, GET /todos, POST /users, POST /todos
# Run with:  uvicorn sqlconnect:app --reload
# pip install fastapi uvicorn
# ---------------------------------------------------------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Re-create an engine for the API layer (previous one was disposed above)
api_engine = create_engine(Host, pool_pre_ping=True)

app = FastAPI(title="Users & Todos API")


class UserIn(BaseModel):
    name: str
    email: str


class TodoIn(BaseModel):
    user_id: int
    title: str
    completed: Optional[bool] = False


@app.get("/users")
def get_users():
    with api_engine.connect() as c:
        rows = c.execute(text("SELECT * FROM users;")).mappings().all()
    return [dict(r) for r in rows]


@app.get("/todos")
def get_todos():
    with api_engine.connect() as c:
        rows = c.execute(text("SELECT * FROM todo where user_id = 4;")).mappings().all()
    return [dict(r) for r in rows]

class Item(BaseModel):
    query: str

@app.post("/postapi")
def get_todos(q:Item):
    with api_engine.connect() as c:
        rows = c.execute(text(q.query)).mappings().all()
    return [dict(r) for r in rows]
