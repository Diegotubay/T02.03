from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

consultas = Table("consultas", meta,
              Column("id",Integer, primary_key=True),
              Column("diagnostico", String(255), nullable=False))
              
  
meta.create_all(engine)