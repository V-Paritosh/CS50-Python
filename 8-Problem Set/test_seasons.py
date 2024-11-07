from seasons import convert, format_str
import pytest

def test_convert():
  assert convert("1999-01-01") == "Thirteen million, six hundred five thousand, one hundred twenty minutes"
  assert convert("1999-12-31") == "Thirteen million, eighty thousand, nine hundred sixty minutes"
  assert convert("1970-01-01") == "Twenty-eight million, eight hundred fifty-seven thousand, six hundred minutes"

def test_invalid_convert():
  with pytest.raises(ValueError):
    convert("01-01-1999")

def test_format_str():
  with pytest.raises(ValueError):
    format_str("January 1, 2000")