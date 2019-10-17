# radforest

# Testing using py.test. 
It's good because it needs the minimal part code to work

## Structure of the test 

Should be at the root level outside the package

package/
    __init__.py
    module/
        __init__.py

    tests/
        __init.py
        *_test.py
        test_*.py

Inside the test.py you should only put definitions with a test_ prefix

def test_Definition_in_Class(val):
    assert val == 1 # this code could be BS

### To execute

pytest ./tests
python -m ./test
