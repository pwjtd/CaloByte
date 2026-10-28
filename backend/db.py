import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool

load_dotenv(".env.local")


def database_url(unpooled: bool = False) -> str:
    url = os.environ["DATABASE_URL_UNPOOLED" if unpooled else "DATABASE_URL"]
    return url.replace("postgresql://", "postgresql+psycopg://", 1)


class Base(DeclarativeBase):
    pass


def make_session():
    engine = create_engine(database_url(), poolclass=NullPool)
    return sessionmaker(engine)