import pandas as pd
import oracledb
from sqlalchemy import create_engine

#Oracle calling
oracledb.init_oracle_client(lib_dir = r"C:\oraclexe\app\oracle\instantclient_19_29")

#DB Conn
Db_conn = create_engine("oracle+oracledb://ETL_Automation:ETL_Automation@localhost:1521/xe")

#query
query = """select * from customer"""

#
df_oracle = pd.read_sql(query,Db_conn)
print(df_oracle)