from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table

metadata = MetaData()

event = Table(
    "event",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String),
    Column("start_date", DateTime, nullable=False),
    Column("end_date", DateTime, nullable=False),
    # Column("location", Strin)
)
