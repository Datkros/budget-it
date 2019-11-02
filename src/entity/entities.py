from sqlalchemy import Column, ForeignKey, MetaData, Sequence, String, Table, Text
from sqlalchemy.dialects

metadata = MetaData()

expense_tbl = Table('expense', metadata,
                    Column('expense_id', String, primary_key=True, index=True),
                    Column('name', String),
                    Column('value', ),
                    Column('currency', String),
                    Column('description', String),
                    Column('expense_date', TIMESTAMP))