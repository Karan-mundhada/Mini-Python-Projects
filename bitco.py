import requests
import json
import sys

try:
    if (len(sys.argv) != 2):
        print("missing Command Line Argument")
        sys.exit()
    x = int(sys.argv[1])

except ValueError:
    print("command-line argument is not a number")
    sys.exit()

else:
    r1 = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = r1.json()
    # print(json.dumps(price, indent=2))
    bitcoin_price =  price["bpi"]["USD"]["rate"]
    print("price of bitcoin =", bitcoin_price*x)