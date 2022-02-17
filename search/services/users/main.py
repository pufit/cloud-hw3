from fastapi import FastAPI

from search.services.users.storage import UserStorage
from search.common import structures
from search.common.config import Config
from search.common.data_source import CSV

app = FastAPI()

config = Config()

storage = UserStorage(CSV(config.users_service_config.data_path))


@app.get("/users/{user_id}", response_model=structures.User)
async def get_user_data(user_id: int):
    return storage.get(user_id)
