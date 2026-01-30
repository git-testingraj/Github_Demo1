import pandas as pd
import pytest
from sqlalchemy import create_engine
import pyodbc

#source data define
@pytest.fixture()
def source_data():
    df_src = pd.read_csv("Data/employees_source.csv")
    return df_src

#Target data define
@pytest.fixture()
def target_data():
    df_trg = pd.read_csv("Data/employees_target.csv")
    return df_trg

#MSSQL Connection
@pytest.fixture()
def MSSQL_Database_connection():
    Db_conn = ("mssql+pyodbc://LAPTOP-R3E5KI54\SQLEXPRESS/HR?"
               "driver=ODBC+Driver+17+for+SQL+Server")

    engine = create_engine(Db_conn)
    query = """select * from employees"""
    df_result = pd.read_sql(query, engine)
    return df_result