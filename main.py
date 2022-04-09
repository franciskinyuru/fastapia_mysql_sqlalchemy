from fastapi import FastAPI
from routes.index import user
from models.user import users
from config.db import meta,engine
app = FastAPI()
meta.create_all(engine)
app.include_router(user)
