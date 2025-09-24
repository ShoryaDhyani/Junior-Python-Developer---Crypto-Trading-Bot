"""
Interactive Binance Bot CLI
Runs in a loop until Ctrl+C
Shows a menu of commands for easier selection
"""

import sys
from src.utils import *
from src.advanced.Advanced import AdvanceBot



COMMANDS_MENU = """
===== Binance Futures CLI =====
Pick a command by typing its number or name:

1. market   - Place a market order
2. limit    - Place a limit order
3. grid     - Place a grid/OCO emulated order
4. stopl    - Place a stop limit order
5. balance  - Check asset balance
6. help     - Show this menu
7. quit     - Exit the CLI
==============================
"""

def handle_command(client:AdvanceBot, cmdline: str):
    parts = cmdline.strip().split()
    if not parts:
        return
    command, *args = parts
    command = command.lower()

    try:
        match command:
            case "1" | "market":
                if len(args) != 3:
                    return print("Usage: market <SYMBOL> <BUY|SELL> <QTY>")
                symbol, side, qty = args
                if not client.validate_symbol(symbol):
                    return
                qty = safe_float(qty, "qty")
                if qty is None: return
                res = client.create_market_order(symbol=symbol, side=side.upper(), quantity=qty)
                print("Initiated tranaction check logs for details")

            case "2" | "limit":
                if len(args) != 4:
                    return print("Usage: limit <SYMBOL> <BUY|SELL> <QTY> <PRICE>")
                symbol, side, qty, price = args
                if not client.validate_symbol(client): 
                    return
                qty = safe_float(qty, "qty")
                price = safe_float(price, "price")
                if qty is None or price is None:
                    return
                res = client.create_limit_order(symbol=symbol, side=side.upper(), quantity=qty, price=price)
                print("Initiated tranaction check logs for details")

            case "3" | "grid":
                if len(args) != 5:
                    return print("Usage: grid <SYMBOL> <QUANTITY> <STEPS> <PRICE> <GRID_SIZE>")
                symbol, qty, steps, tp, gs = args
                if not client.validate_symbol(symbol): return
                steps = safe_float(steps, "steps")
                qty=safe_float(qty,"qty")
                tp = safe_float(tp, "tp_price")
                gs=safe_int(gs,"grid_size")
                if None in (qty, tp): return
                res = client.grid_orders(symbol=symbol,step=steps, base_price=tp,grid_size=gs,quantity=qty)
                print("Initiated tranaction check logs for details")

            case "4" | "stopl":
                if len(args) != 5:
                    return print("Usage: stopl <SYMBOL> <BUY|SELL> <TOTAL_QTY> <START PRICE> <STOP_PRICE>")
                symbol, side, qty,price, stop_price = args
                if not client.validate_symbol(symbol):
                    return
                if None in (qty,stop_price,side): return
                res = client.stop_limit_order(symbol=symbol, side=side.upper(),quantity=qty, stop_price=stop_price,price=price)
                print("Initiated tranaction check logs for details")
            case "5" | "balance":
                if len(args) != 1:
                    return print("Usage: balance <ASSET>")
                bal = client.get_balance(args[0])
                if bal is not None:
                    print(f"Balance {args[0].upper()}: {bal}")

            case "6" | "help":
                print(COMMANDS_MENU)

            case "7" | "quit" | "exit":
                print("Exiting CLI.")
                sys.exit(0)

            case _:
                print(f"Unknown command: {command}. Type 'help' for list.")

    except Exception as e:
        log_error(f"Handel_command func {e}")

def main():
    api_key, api_secret = load_api_keys()
    client = AdvanceBot(api_key, api_secret, testnet=True)

    print("🚀 Binance Futures CLI (type 'help' or number for commands, 'quit' to exit)")
    print(COMMANDS_MENU)

    try:
        while True:
            cmdline = input(">> ")
            handle_command(client, cmdline)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected, exiting.")


if __name__ == "__main__":
    main()
