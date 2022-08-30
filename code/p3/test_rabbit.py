import os
import os.path
import pytest
import pandas as pd
import main
"""
run from command line with
pytest test_rabbit.py
"""
@pytest.fixture
def setup():
    if os.path.isfile("rabbits.csv"):
        os.remove("rabbits.csv")
    main.main()
    
@pytest.fixture
def teardown():
   if os.path.isfile("rabbits.csv"):
       os.remove("rabbits.csv")

def test_file_exists():
      assert os.path.isfile("rabbits.csv")

def test_comments():
    fin = open("rabbits.csv")
    lines = fin.readlines()
    fin.close()
    assert "# Table of rabbit pairs" == lines[0].strip()
    assert "# Cages will run out in month 14" == lines[-1].strip()

def test_data():
    data = [
    [1, 1, 0, 1],
    [2, 1, 1, 2],
    [3, 2, 1, 3],
    [4, 3, 2, 5],
    [5, 5, 3, 8],
    [6, 8, 5, 13],
    [7, 13, 8, 21],
    [8, 21, 13, 34],
    [9, 34, 21, 55],
    [10, 55, 34, 89],
    [11, 89, 55, 144],
    [12, 144, 89, 233],
    [13, 233, 144, 377],
    [14, 377, 233, 610]
    ]
    df_expected = pd.DataFrame(data,columns=['Month', 'Adults', 'Babies', 'Total'])
    df_actual = pd.read_csv("rabbits.csv", comment='#')
    assert df_expected.equals(df_actual)

def test_code_quality():
    from pylint import epylint as lint
    (pylint_stdout, pylint_stderr) = lint.py_run('main.py', return_std=True)
    expected = "Your code has been rated at 10.00/10"
    actual = pylint_stdout.getvalue()
    assert expected in actual
    
