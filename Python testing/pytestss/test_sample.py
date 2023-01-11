import pytest

'''
-->pytest is a software test framework, which means pytest is a command-line tool
   that automatically finds tests you've written, runs the tests,
   and reports the results
-->pytest identifies the test files and test cases which contains prefix as 'text'
   in a directory
--> Command to execute tests:
    syntax: pytest  --> this runs all tests in a repo
    syntax: pytest test_file_path  --> this runs tests of specific file
--> 'py.test' is also be used as 'pytest' command to execute tests
--> No need to remember multiple assert statements when compared with unitest
--> Simply we can use assert to test the cases

--> pytest does not follow the alphabetical order to execute the tests
--> pytest executes the tests based on the order we defined while writing tests
--> To see the order of tests execution:
    syntax: 'pytest -v'
--> To execute only specific tests(-k)
    syntax: 'pytest -v -k "sub_string_of_test_name"'
    - This will execute the tests which contains the specified substring in the command
    - We can test by seraching multpile strings by applying 'and' 'or' conditions
    syntax: 'pytest -v -k "sub_string_of_test_name or "sub_string_of_test_name"'"'
    syntax: 'pytest -v -k "sub_string_of_test_name and "sub_string_of_test_name"'"'
    
--> Execute the tests in quite mode(-q):
    syntax: pytest -q
    
--> Python debugger in pytest(pdb):
    syntax: pytest --pdb
--> Want python debugger for every test case (--trace) will be used
    syntax: python --trace
'''


def test_string():
    str1 = 'pytest'
    str2 = 'pytest'
    assert str1 == str2


def test_type():
    str1 = 'pytest'
    str2 = 'pytest'
    assert type(str1) == type(str2)


# To halt(-x) or stop the test when failure happens and to stop all remaining
# test cases which existed after the failure test case
# syntax: pytest -x
# --maxfail=2 :syntax: pytest -x --maxfail=2
#  this will stop the test cases execution when max 2 test case failure occurs
# traceback(-tb): to traceback test case failre details
# syntax: pytest -x -tb=no or auto or short
def test_addition():
    a = 7
    b = 5
    assert a + b == 17


def test_sub_string():
    str1 = "pytest"
    str2 = "py"
    assert str2 in str1


'''
Executing tests using test markers(-m)
1. tests can be executes using pytest markers
    syntax: 'pytest -m number'
    This will execute the tests which contains the pytest marker as number
'''


@pytest.mark.number
def test_multiplication():
    a = 7
    b = 5
    assert a * b == 35


@pytest.mark.string
def test_string_length():
    str1 = "pytest"
    str2 = "pytest"
    assert len(str2) == len(str2)


# Skip tests using skip
@pytest.mark.skip(reason='Skipped Temporarily')
def test_string_eqality():
    str1 = "pytest"
    str2 = "pytest"
    assert str1 == str2
