from sqlalchemy import Table, Column, Integer, BigInteger, String, Text, DateTime, MetaData
from datetime import datetime

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("social_id", BigInteger, nullable=False),
    Column("username", String(50)),
    Column("registration_date", DateTime, nullable=True, default=datetime.utcnow),
    Column("taps", BigInteger, default=0),
    Column("name", Text, nullable=True),
    Column("info", Text, nullable=True),
    Column("photo", Text, nullable=True),
)