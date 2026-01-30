import pandas as pd
import pytest

#Data validation

def test_data_validation_src_trg(source_data,target_data):
 assert source_data.equals(target_data),"Data is not matching"

 #Duplicate data

def test_duplicate_data_in_source_target(source_data,target_data):
 source_duplicate_count = source_data.duplicated().sum()
 target_duplicate_count = target_data.duplicated().sum()
 assert source_duplicate_count == 0, "Duplicate record are available in the Source"
 assert target_duplicate_count == 0, "Duplicate record are available in the Target"

#Duplicate data check in DB table
def test_DB_table_duplicate_check(MSSQL_Database_connection):
 assert MSSQL_Database_connection.duplicated().sum() == 0,"Duplicate record in DB Table"
