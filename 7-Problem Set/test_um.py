from um import count
import pytest

def test_valid_count():
  assert count("um") == 1
  assert count("um?") == 1
  assert count("Um, thanks for the album.") == 1
  assert count("Um, thanks, um...") == 2

def test_invalid_without_um_count():
  assert count("hello") == 0

def test_invalid_with_um_count():
  assert count("yumm") == 0
  assert count("umm") == 0