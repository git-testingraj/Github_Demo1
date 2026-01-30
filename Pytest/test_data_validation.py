#with hard assertion and without fixture
import pandas as pd
import pytest

'''
def test_data_validation_between_source_target():
    df_source = pd.read_csv("Data/employees_source.csv")
    df_target = pd.read_csv("Data/employees_target.csv")

    assert df_source.equals(df_target),"Data is not matching"

def test_duplicate_data_in_source_target():
    df_source = pd.read_csv("Data/employees_source.csv")
    source_duplicate_count = df_source.duplicated().sum()
    df_target = pd.read_csv("Data/employees_target.csv")
    target_duplicate_count = df_target.duplicated().sum()

    assert source_duplicate_count == 0 ,"Duplicate record are available in the Source"
    assert target_duplicate_count == 0, "Duplicate record are available in the Target"
'''

#with fixture

@pytest.mark.regression
def test_data_validation_between_source_target(source_data,target_data):
    assert source_data.equals(target_data),"Data is not matching"

@pytest.mark.regression
@pytest.mark.smoke
def test_duplicate_data_in_source_target(source_data,target_data):
    source_duplicate_count = source_data.duplicated().sum()
    target_duplicate_count = target_data.duplicated().sum()
    assert source_duplicate_count == 0 ,"Duplicate record are available in the Source"
    assert target_duplicate_count == 0, "Duplicate record are available in the Target"

@pytest.mark.skip
def test_markertest1():
    assert 1 == 2,"number is not equal"

@pytest.mark.xfail
@pytest.mark.smoke
def test_markertest2():
    print("Need to execute but dont give an error.")
    assert 10 >= 20, "Number is not small then 20"