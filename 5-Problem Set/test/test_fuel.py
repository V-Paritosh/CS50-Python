from fuel import convert 
from fuel import gauge
import pytest

def test_convert_vaild():
  assert convert("1/2") == 50
  assert convert("0/1") == 0
  assert convert("1/1") == 100

def test_convert_invaild():
  with pytest.raises(ValueError):
    convert("2/1")
  with pytest.raises(ValueError):
    convert("a/b")
  with pytest.raises(ZeroDivisionError):
    convert("1/0")

def test_gauge():
  assert gauge(0) == "E"
  assert gauge(1) == "E"
  assert gauge(100) == "F"
  assert gauge(99) == "F"
  assert gauge(50) == "50%"