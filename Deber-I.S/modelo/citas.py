from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Date, Time, CHAR
from config.db import engine, meta

citas = Table("citas", meta,
              Column("id",Integer, primary_key=True),
              Column("fecha", Date, nullable=False),
              Column("hora", Time, nullable=False),
              Column("estado", CHAR, nullable=False))


meta.create_all(engine)