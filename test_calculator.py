from calculator import add, sub, mul, div
#import pytest
import random

'''
create a new file called test_calculator.py and write unit tests for each
function in calculator.py. Use the assert statement and include tests for both normal cases and edge
cases (like division by zero).

'''
for x in range(20):
    a, b = random.randint(0, 100), random.randint(0, 100)
    result = a + b
    try:
        assert result == add(a, b)
    except AssertionError as e:
        print(e)

    print(result)



try:
    assert 234 == add(5, 5)
except AssertionError as e:
    print("er")