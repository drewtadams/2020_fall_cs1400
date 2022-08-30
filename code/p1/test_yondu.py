import pytest
import main
"""
Test new CS 1400 Project 1: Yondu Udonta.
run from command line with
pytest test_yondu.py
Note: capsys is a built-in pytest fixture,
"""

def in_f(idx):
    '''this function is a generator of test input values.'''
    values = [
        "20\n",
        "1000\n",
        "35\n",
        "100000\n",
        "10\n",
        "0\n",
        "2\n",
        "100000\n",
        "aaa\n",
        "100000\n",
         "20\n",
        "bbbb\n",
        "-20\n",
        "1000\n",
        "20\n",
        "-1000\n",
        "20.0\n",
        "1000\n",
        "20\n",
        "1000.0\n",
        "20\n",
        "59\n",
       ] 
    i = idx
    while i < len(values):
        yield values[i]
        i +=1
    
@pytest.mark.parametrize("test_input, expected", [
    (in_f(0), "Yondu's share: 158\nPeter's share: 126\nCrew: 36\nRBF: 14\n"),
    (in_f(2),"Yondu's share: 15197\nPeter's share: 11770\nCrew: 2210\nRBF: 4\n"),
    (in_f(8),"Enter positive integers for reavers and units.\n"),
    (in_f(6),"Not enough crew.\n"),
    (in_f(8),"Enter positive integers for reavers and units.\n"),
    (in_f(10),"Enter positive integers for reavers and units.\n"),
    (in_f(12),"Enter positive integers for reavers and units.\n"),
    (in_f(14),"Enter positive integers for reavers and units.\n"),
    (in_f(16),"Enter positive integers for reavers and units.\n"),
    (in_f(18),"Enter positive integers for reavers and units.\n"),
    (in_f(20),"Not enough units.\n"),
    ])
def test_splitup(test_input,expected,monkeypatch,capsys):
    ''' This function is decorated with pairs of (input,expected output) tuples.
    Inputs are indexed by the generator in_f above, and the console
    output is captured by capsys.
    '''
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda p: next(test_input))
        main.main()
        actual, err = capsys.readouterr()
        print(expected)
        print(actual)
        assert actual == expected

def test_code_quality():
    from pylint import epylint as lint
    (pylint_stdout, pylint_stderr) = lint.py_run('main.py', return_std=True)
    expected = "Your code has been rated at 10.00/10"
    actual = pylint_stdout.getvalue()
    assert expected in actual