import json
from collections import namedtuple

from src.conf.settings import redis

Product = namedtuple("Product", ["id", "name", "price"])


async def set_cache(key: str, value: dict):
    """Setting cache data"""
    value_json = json.dumps(value)
    value = await redis.set(key, value_json)
    return value


async def get_cache(key: str) -> dict:
    """Getting cache data by key"""
    value = redis.get(key)
    if not value:
        raise ValueError(f"Not product with id {key}")
    value_dict = json.loads(value)
    return value_dict
