from twttr import shorten

def test_word():
  assert shorten("Twitter") == "Twttr"

def test_phrase():
  assert shorten("What's your name?") == "Wht's yr nm?"

def test_no_vowel():
  assert shorten("CS50") == "CS50"

def test_upper():
  assert shorten("AEIOU") == ""