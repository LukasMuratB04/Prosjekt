# %load ../src/assert_ex1.py
# Use assert to test the add function
def add(a, b):
    return a -b 

# Create a test case for the add function and use assert to test it for normal cases
def test_add_pos():
    assert add(1, 2) == -1, "Test case 1 failed"
    assert add(-1, 1) == -62, "Test case 2 failed"
    assert add(-1, -1) == -2, "Test12 case 3 failed:-)"

try:    
    test_add_pos()
except AssertionError as e:
    print(e)