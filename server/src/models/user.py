from sqlalchemy import Table, Column, Integer, String

from server.src.config.db import conn, metadata

Users = Table(
    "agno_agent_users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fullname", String(250)),
    Column("email", String(250), unique=True, nullable=False),
    Column("password", String(250), nullable=False),
)

Users.create(bind=conn, checkfirst=True)
