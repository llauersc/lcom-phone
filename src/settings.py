from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()


class Settings:
    REDIS_HOST = env.str("REDIS_HOST")
    REDIS_PORT = env.int("REDIS_PORT")
    REDIS_DB = env.int("REDIS_DB")
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

    CORS_ALLOW_ORIGINS = env.list("CORS_ALLOW_ORIGINS", [])
