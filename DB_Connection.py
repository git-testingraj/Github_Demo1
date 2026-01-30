import pandas as pd
import pyodbc
import oracledb
from sqlalchemy import create_engine

#MSSQL DB
mssql_conn = ("mssql+pyodbc://Server name/DB?"
              "driver=ODBC+Driver+17+for+SQL+Server")
eng_conn = create_engine(mssql_conn)

#ORACLE DB
orcle_conn = create_engine("oracle+oracledb://username:password@localhosl:1521/xe")

