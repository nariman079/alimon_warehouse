import asyncio
import sys
from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from redis import Redis
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv(override=True)


current_directory: Path = Path.cwd()

if sys.platform == "win32":  
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


DEBUG = getenv("DEBUG") == '1'

POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_HOST = getenv("POSTGRES_HOST")
POSTGRES_PORT = getenv("POSTGRES_PORT")

REDIS_HOST = getenv("REDIS_HOST", 'localhost')
REDIS_PORT = getenv("REDIS_PORT", 6379)

ALGORITHM = getenv('ALGORITHM', 'HS256')
SECRET = getenv('SECRET_KEY', 'secret')

DB_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

ZOOKEEPER_CLIENT_PORT = getenv("ZOOKEEPER_CLIENT_PORT")
ZOOKEEPER_TICK_TIME = getenv("ZOOKEEPER_TICK_TIME")

KAFKA_BROKER_ID = getenv("KAFKA_BROKER_ID")
KAFKA_ZOOKEEPER_CONNECT = getenv("KAFKA_ZOOKEEPER_CONNECT")
KAFKA_ADVERTISED_LISTENERS = getenv("KAFKA_ADVERTISED_LISTENERS")
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR = getenv(
    "KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR"
)
KAFKA_BROKERCONNECT = getenv("KAFKA_BROKERCONNECT")


engine = create_async_engine(
    DB_URL,
    pool_recycle=280,  
    echo=not PRODUCTION_MODE,
)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)