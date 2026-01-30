import pandas as pd
import pytest

def test_src_trg_data_match(source_data_load,target_data_load):
    assert source_data_load.equals(target_data_load),"Data is not matching"

def test_duplicate_data_in_source_target(source_data_load,target_data_load):
    source_duplicate_count = source_data_load.duplicated().sum()
    target_duplicate_count = target_data_load.duplicated().sum()
    assert source_duplicate_count == 0 ,"Duplicate record are available in the Source"
    assert target_duplicate_count == 0, "Duplicate record are available in the Target"