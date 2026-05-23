import redis
import json
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class RedisCache:
    def __init__(self):
        self.redis_client = redis.Redis.from_url(
            settings.REDIS_URL,
            decode_responses=True
        )
    
    def set_cache(self, key: str, value: any, ttl: int = 3600):
        """Set cache with TTL"""
        try:
            self.redis_client.setex(
                key,
                ttl,
                json.dumps(value)
            )
            logger.info(f"Cache set: {key}")
        except Exception as e:
            logger.error(f"Cache set error: {e}")
    
    def get_cache(self, key: str):
        """Get value from cache"""
        try:
            value = self.redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Cache get error: {e}")
            return None
    
    def delete_cache(self, key: str):
        """Delete cache key"""
        try:
            self.redis_client.delete(key)
            logger.info(f"Cache deleted: {key}")
        except Exception as e:
            logger.error(f"Cache delete error: {e}")

redis_cache = RedisCache()