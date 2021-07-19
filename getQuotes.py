#---------------------------------------------------------#
# getQuotes.py						  					  
# Author: Pirate					  					  
#---------------------------------------------------------#
#---------------------------------------------------------#
# Gets quotes from an array of symbols.			  		  
# Saves quotes in seperate folders for each symbol.       
# 							  							  	
# Setup and Run:					  					  
# 1) Set your CoinAPI API key in the 'apiKey' variable.   
# 2) Set symbols to gather quotes for in the symbolArray. 
# 3) Run the script with: python3 getQuotes.py            
#---------------------------------------------------------#
import os
import json
import requests
from datetime import datetime
from json.decoder import JSONDecodeError
#---------------------------------------------------------#
# Configuration:                                          
#---------------------------------------------------------#
apiKey = "YOUR-COINAPI-KEY-HERE" # CoinAPI API Key

# Symbols to get quotes for
symbolArray = [
	"COINBASE_SPOT_ETH_USD",
	 "COINBASE_SPOT_BTC_USD",
	  "COINBASE_SPOT_ATOM_USD",
	  "KUCOIN_SPOT_LOCG_USDT",
	  "KUCOIN_SPOT_OOE_USDT",
	  "KUCOIN_SPOT_CRO_USDT",
	  "COINEX_SPOT_BAN_USDT",
	  "BINANCE_SPOT_HNT_USDT"]
#---------------------------------------------------------#
# DONT EDIT BELOW THIS NOTICE				  		      
#---------------------------------------------------------#
now = datetime.now() # Current Date/Time
time = now.strftime("%H:%M:%S") # Time as String
homeDir = os.path.dirname(__file__) # Home Directory
# Make folder, get quote and save json output for each symbol in array
for x in symbolArray:
	url = "https://rest.coinapi.io/v1/quotes/" + x + "/current" # URL to send request
	headers = {'X-CoinAPI-Key' : apiKey} # Request header - CoinAPI Key
	response = requests.get(url, headers=headers) # Request Response
	symbolJSON = response.json() # Request Response as JSON
	symbolDir = os.path.join(homeDir, x) # Symbol Directory
	symbolFile = x + "_" + time + ".json" # Symbol File
	symbolFilePath = os.path.join(symbolDir, symbolFile) # Symbol File Path
	
	# Try to create symbol directory.
	# If doesn't already exist, create directory and output success message.
	# If already exists, output warning message.
	try:
		os.mkdir(symbolDir)
		print("[Success] Data Directory Created: " + symbolDir)
	except OSError as error:
		print("[Warning] Data Directory Exists: " + symbolDir)

	# Try to create new file with symbol's quote from request response as JSON.
	# If doesn't already exist, create file, dump JSON request response and output success message.
	# If already exists, output warning message.
	try:
		with open(symbolFilePath, 'w') as symbolData:
    			json.dump(symbolJSON, symbolData)
		print("[Success] Data File Created: " + symbolFilePath)
	except json.decoder.JSONDecodeError:
		print("[Warning] Error Creating Data File: " + symbolFilePath)
