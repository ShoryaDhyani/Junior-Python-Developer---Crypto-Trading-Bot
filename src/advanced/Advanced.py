from ..bot import Bot
from ..utils import *
import asyncio

class AdvanceBot(Bot):

    def stop_limit_order(self,symbol:str,quantity:float,side:str,price:str,stop_price:str):
        symbol=symbol.upper()
        log_info(f"Initiating Stop Limit Order to {side} {quantity} {symbol} at stop price {stop_price}")
        try:
            ord=self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )
            log_info(f"Stop Limit Order Placed to {side}, Api Response {ord}")
        except Exception as e:
            log_error(e)
    
    async def twap_order(self,symbol:str, side:str, quantity, slices, interval):
        symbol=symbol.upper()
        log_info(f"Initiating TWAP Order to {side} {slices} slices for {quantity} {symbol} at interval of {interval}sec ")
        try:
            slice_qty = quantity / slices
            for i in range(slices):
                self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=round(slice_qty, 3)
                )
                log_info(f"Slice {i+1}/{slices} executed.")
                await asyncio.sleep(interval)
        except Exception as e:
            log_error(e)
    

    def grid_orders(self,symbol, base_price, grid_size, step, quantity):
        symbol=symbol.upper()
        log_info(f"Initiating Grid Order for {quantity} {symbol} of gride size {grid_size}")
        orders = []
        try:
            #  Buy orders below price
            for i in range(1, grid_size+1):
                buy_price = base_price - (i * step)
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side="BUY",
                    type="LIMIT",
                    price=str(buy_price),
                    quantity=quantity,
                    timeInForce="GTC"
                )
                orders.append(order)

            # Sell orders above price
            for i in range(1, grid_size+1):
                sell_price = base_price + (i * step)
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side="SELL",
                    type="LIMIT",
                    price=str(sell_price),
                    quantity=quantity,
                    timeInForce="GTC"
                )
                orders.append(order)
            for i, o in enumerate(orders):
                log_info(f"Grid order {i}: {o}")
        except Exception as e:
            log_error(e)
        return orders