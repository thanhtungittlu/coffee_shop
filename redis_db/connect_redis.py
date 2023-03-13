import redis
from config import config

r = redis.Redis(
    host=config.SERVER_REDIS,
    port=config.PORT_REDIS,
)