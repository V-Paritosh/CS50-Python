from numb3rs import validate
import pytest

def test_valid_ip():
  assert validate("127.0.0.1") == True
  assert validate("255.255.255.255") == True

def test_invalid_ip():
  assert validate("512.512.512.512") == False
  assert validate("1.2.3.1000") == False
  assert validate("-1.56.567.-") == False
  assert validate("cat") == False

def test_invalid_ip_len():
  assert validate("8.8.8") == False
  assert validate("10.10.10.10.10") == False