# CoinAPI-Python
Python scripts using CoinAPI to gather cryptocurrency quotes and exchange data. Gets quotes from an array of symbols. Saves quotes in seperate folders for each symbol.       
							  							  	
**Setup and Run:**					  					  
1) Set your CoinAPI API key in the 'apiKey' variable.

```python3
#Just copy/paste your CoinAPI key in the quotes:
apiKey = "YOUR-COINAPI-KEY-HERE" # CoinAPI API Key
```

2) Set symbols to gather quotes for in the symbolArray.

```python3
#Symbol/Exchange Structure:
#exchangeName_spotMarket/perpetualMarket/etc_fromCoin_toCoin
COINBASE_SPOT_BTC_USD #Coinbase Spot BTC/USD
BINANCE_PERP_BTC_USDT #Binance Perpetuals BTC/USDT
```

```python3
#Symbol/Exchange Examples:
symbolArray = [
	"COINBASE_SPOT_ETH_USD", #Coinbase ETH/USD
	 "COINBASE_SPOT_BTC_USD", #Coinbase BTC/USD
	  "COINBASE_SPOT_ATOM_USD", #Coinbase ATOM/USD
	  "KUCOIN_SPOT_LOCG_USDT", #Kucoin LOCG/USDT
	  "KUCOIN_SPOT_OOE_USDT", #Kucoin OOE/USDT
	  "KUCOIN_SPOT_CRO_USDT", #Kucoin CRO/USDT
	  "COINEX_SPOT_BAN_USDT", #Coinex BAN/USDT
	  "BINANCE_SPOT_HNT_USDT"] #Binance HNT/USDT
```
Full list of exchange market combos can be found here:
https://docs.coinapi.io/#excel-g-sheets

3) Run the script with: 
```bash
python3 getQuotes.py            
```

---

More information about CoinAPI's... API:
https://docs.coinapi.io/
