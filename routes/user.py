from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()


@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()


@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.post("/")
async def write_data(new_user: User):
    conn.execute(users.insert().values(
        name=new_user.name,
        email=new_user.email,
        password=new_user.password
    ))
    return conn.execute(users.select()).fetchall()


@user.put("/{id}")
async def update_data(id: int, update_u: User):
    conn.execute(users.update().values(
        name=update_u.name,
        email=update_u.email,
        password=update_u.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user.delete("/{id}")
async def delete_data(id):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()