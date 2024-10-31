import sys
import requests
import json

try:
    if not(sys.argv[1]):
        print("Missing command-line argument")
        sys.exit()
    if not sys.argv[1] is not int:
        print("Command-line argument is not a number")

    bitcon = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcon = bitcon.json()

    value = bitcon["bpi"]["USD"]["rate_float"]


    value = value * float(sys.argv[1])
    print(f"${value:,.4f}")
except requests.RequestException:
    sys.exit()
