import pandas as pd
import pyodbc
from sqlalchemy import create_engine

#DB Connection

database_connection = (
    "mssql+pyodbc://LAPTOP-R3E5KI54\SQLEXPRESS/HR?"
    "driver=ODBC+Driver+17+for+SQL+Server"
)

#Create engine
engine = create_engine(database_connection)

#SQL Query
query = """select * from employees"""
df = pd.read_sql(query,engine)
print(df)