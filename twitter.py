import re

url = input("URL: ").strip()
print(url)

username = re.sub(r"(^https?://)?(www\.)?twitter\.com/", "", url)
matches = re.search(r"^https?://(?:www\.)?twitter.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
  username = matches.group(1)
print(f"Username: {username}")