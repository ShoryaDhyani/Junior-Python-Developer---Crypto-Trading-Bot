from binance.client import Client
import time
import sys
from .utils import *
import asyncio

class Bot:
    def __init__(self,api_key,api_secret,testnet=True,):
        try:
            self.client=Client(api_key=api_key,api_secret=api_secret,testnet=testnet,tld='com')
            if testnet: self.client.FUTURES_URL='https://testnet.binancefuture.com/fapi'
            self.client.TIME_OFFSET = self.client.get_server_time()['serverTime'] - int(time.time() * 1000)
            print(self.client.futures_ping())
        except Exception as e:
            log_error(e)
            print("Error Occured")
            sys.exit(1)

    def validate_symbol(self,symbol: str) -> bool:
        if symbol not in [s['symbol'] for s in self.client.futures_exchange_info()['symbols']]:
            log_error("Invalid Symbol")
        return True


    def printprice(self,symbol:str):
        ticker=self.client.get_symbol_ticker(symbol=symbol.upper())
        return float(ticker['price'])

    def get_balance(self,asset:str=None):
        try:
            res = self.client.futures_account_balance()
            for b in res:
                if b["asset"].upper() == asset.upper():
                    return float(b["availableBalance"])
            log_error(f"Asset {asset} not found in balance.")
        except Exception as e:
            log_error(f"Failed to fetch balance: {e}")
        return None
        
    
    def create_market_order(self,quantity:float,symbol:str,side:str):
        symbol=symbol.upper()
        log_info(f"Initiating Market Order to {side} {quantity} {symbol}")
        try:
            ord=self.client.futures_create_order(quantity=quantity,
                symbol=symbol,
                type="MARKET",
                side=side
                )
            log_info(f"Order confirmed to {side}, Api Response {ord}")
            return ord
        except Exception as e:
            log_error(e)


    def create_limit_order(self,quantity:float,symbol:str,price:float,side:str,inforce:str="GTC"):
        symbol=symbol.upper()
        log_info(f"Initiating Limit Order to {side} {quantity} {symbol}")
        try:
            ord=self.client.futures_create_order(symbol=symbol,
                quantity=quantity,
                type="LIMIT",
                price=price,
                timeInForce=inforce,
                side=side
                )
            log_info(f"Created Limit {side} Order for {quantity} {symbol} at {price}, Api Response {ord}")
            return ord
        except Exception as e:
            log_error(e)

