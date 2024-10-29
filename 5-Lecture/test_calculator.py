import pytest
from calculator import square

def test_positive():
  assert square(2) == 4
  assert square(3) == 9

def test_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_zero():
  assert square(0) == 0

def test_str():
  with pytest.raises(TypeError):
    assert square("cat")


'''
Version 1
def test_square():
  try:
    assert square(2) == 4
  except:
    print("2 squared wasn't 4")
  try:
    assert square(3) == 9
  except:
    print("3 squared wasn't 9")

Version 2
def test_square():
  assert square(2) == 4
  assert square(3) == 9
  assert square(-2) == 4
  assert square(-3) == 9
  assert square(0) == 0
'''