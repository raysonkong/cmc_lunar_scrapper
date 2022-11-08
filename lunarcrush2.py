from requests import Request, Session
import requests

import json
import pprint
import datetime
import time
import os
from config_lc2 import *

SLEEP_TIME = 0.2	

## ==================================##
## setup config_lc2.py in the same folder
## ==================================##

## ================ ##
## Notes on Config ## 
## ================ ##
  ## to be edited later
  ## each Lunar page has 100 coins
  ## each txt file represents one CMC Page
  ## and each symbol produces n * 2 outputs(BTC and USDT pairs)
  ## Hence each page produces n * 2 * 100 outputs
  ##(n=num of exchanges, 2 represents BTC and USDT pairs
  ## e.g 4 exchanges, each cmc page produces 4 * 2 * 100 = 800 outputs(trading pairs) in each txt file

 ## each additional exchange is 
    ## an extra 2 outputs for each pair
    ## Hence an extra 200 output for each page/txt file
 ## so max 5 exchange is allowed to keep each list < 1000

## ==============##
## Config Code  ## 
## ==============## 

## HOW_MANY_COINS Determine how many coins you are getting from CMC
## EXCHANGES determines exhanges you want

# HOW_MANY_COINS = 4000
# EXCHANGES=["BINANCE", "KUCOIN", 'BITTREX', 'HUOBI']


## Do not alter below easily

## Tradingview Lists limited by 1000 output per file
## GROUP_SIZE determines output number per text file

# GROUP_SIZE = len(EXCHANGES) * 200
## CURRENCIES determine the trading pairs
# CURRENCIES = ['BTC', 'USDT']
# API_KEY = 'Your Api Key'
# URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

## end of Config file


#===== Setup Date and Time #======== 
# Date
generation_date = datetime.datetime.now()
generation_date = generation_date.strftime("%d_%m_%Y")


# Time now
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
#print(current_time)


#generation_time = now.strftime("%H:%M:%S")

## API Call ### 
import requests

url = URL
headers = {
  'Authorization': API_KEY
}

parameters = {
	'limit': HOW_MANY_COINS
}

response = requests.request("GET", url, headers=headers,params=parameters)
data = response.text.encode('utf8')

parsedResponse = json.loads(data.decode('utf-8'))['data']
#print(parsedResponse[0]['s'])

#================================================ # 
# Step 1 #
# Turn Json response to a list of symbols
# [ 'BTC', "ETH", ...] 

symbols = []
def json_to_tickers(data):
    for item in data:
        symbols.append(item["s"])

json_to_tickers(parsedResponse)
print(symbols)

# now symbols hold all our ..well.. symbols

