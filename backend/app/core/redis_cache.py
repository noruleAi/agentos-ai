import redis

from app.core.config import settings

redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)

def set_cache(key, value):

    redis_client.set(key, value)

def get_cache(key):

    return redis_client.get(key)