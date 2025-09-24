# Binance Futures CLI Bot

🚀 **Interactive Python CLI bot for Binance Futures (Spot coming soon!)**

This project is a Python-based trading bot for **Binance Futures**, supporting **market, limit, OCO, and TWAP orders**. It features a fully interactive CLI, asynchronous order execution, and live balance checks. Designed for both **testnet** and **mainnet** (with proper API keys).

---

## Features

* ✅ Place **Market Orders**
* ✅ Place **Limit Orders**
* ✅ Emulate **OCO (One-Cancels-the-Other) orders**
* ✅ Execute **Stop Limit orders**
* ✅ Check account **balance** for any asset
* ✅ Interactive **menu with commands** and help
* ✅ Robust error handling and logging

---

## Requirements

* Python 3.10+
* pip libraries:

  ```bash
  pip install python-binance asyncio
  ```
* Binance Futures **API key and secret** (Testnet recommended for practice)

---

## Installation

1. Clone the repository:

```bash
git clone <repo_url>
cd <repo_folder>
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your API keys in `src/utils.py` (or environment variables):

```python
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
```

---

## Usage

Run the CLI:

```bash
python runme.py
```

You will see an interactive prompt:

```text
🚀 Binance Futures CLI (type 'help' for commands, 'quit' to exit)
>>
```

### Commands

| Command             | Description                       | Example                      |                                    |
| ------------------- | --------------------------------- | ---------------------------- | ---------------------------------- |
| \`market SYMBOL BUY | SELL QTY\`                        | Place a market order         | `market BTCUSDT BUY 0.01`          |
| \`limit SYMBOL BUY  | SELL QTY PRICE\`                  | Place a limit order          | `limit BTCUSDT SELL 0.01 28000`    |
| \`oco SYMBOL BUY    | SELL QTY TP\_PRICE SL\_PRICE\`    | Place an emulated OCO order  | `oco BTCUSDT BUY 0.01 30000 27000` |
| \`twap SYMBOL BUY   | SELL TOTAL\_QTY SLICES INTERVAL\` | Place a TWAP order over time | `twap BTCUSDT BUY 0.1 5 10`        |
| `balance ASSET`     | Check account balance             | `balance USDT`               |                                    |
| `help`              | Show command list                 | `help`                       |                                    |
| `quit` / `exit`     | Exit the bot                      | `quit`                       |                                    |

> All commands execute asynchronously — the CLI will not block while orders are processed.

---

## Notes

* **Testnet vs Mainnet**:

  * Testnet URL: `https://testnet.binancefuture.com`
  * Live URL: `https://fapi.binance.com`
  * Ensure correct API keys for the network you are using.

* **Order Restrictions**:

  * Minimum notional value: 100 USD per order
  * Stop Limit orders cannot trigger immediately — ensure stop price is not already reached

* **Async Execution**:
  The bot uses Python `asyncio` to allow orders to process without blocking the CLI menu.

---

## Logging

All events and errors are logged to the console:

```text
2025-09-24 15:05:05,612 [INFO] Initiating Stop Limit Order to BUY 0.01 BTCUSDT at stop price 113000
2025-09-24 15:05:06,170 [INFO] Stop Limit Order Placed to BUY, Api Response {'orderId': 5678026699, 'symbol': 'BTCUSDT', 'status': 'NEW', 'clientOrderId': 'x-Cb7ytekJdfe1a77b4fd46509340719', 'price': '113010.00', 'avgPrice': '0.00', 'origQty': '0.010', 'executedQty': '0.000', 'cumQty': '0.000', 'cumQuote': '0.00000', 'timeInForce': 'GTC', 'type': 'STOP', 'reduceOnly': False, 'closePosition': False, 'side': 'BUY', 'positionSide': 'BOTH', 'stopPrice': '113000.00', 'workingType': 'CONTRACT_PRICE', 'priceProtect': False, 'origType': 'STOP', 'priceMatch': 'NONE', 'selfTradePreventionMode': 'EXPIRE_MAKER', 'goodTillDate': 0, 'updateTime': 1758706505791}
2025-09-24 15:24:00,485 [INFO] Initiating Market Order to BUY 0.1 BTCUSDT
2025-09-24 15:24:01,012 [INFO] Order confirmed to BUY, Api Response {'orderId': 5678036954, 'symbol': 'BTCUSDT', 'status': 'NEW', 'clientOrderId': 'x-Cb7ytekJ73c163d59e0424917b5e6d', 'price': '0.00', 'avgPrice': '0.00', 'origQty': '0.100', 'executedQty': '0.000', 'cumQty': '0.000', 'cumQuote': '0.00000', 'timeInForce': 'GTC', 'type': 'MARKET', 'reduceOnly': False, 'closePosition': False, 'side': 'BUY', 'positionSide': 'BOTH', 'stopPrice': '0.00', 'workingType': 'CONTRACT_PRICE', 'priceProtect': False, 'origType': 'MARKET', 'priceMatch': 'NONE', 'selfTradePreventionMode': 'EXPIRE_MAKER', 'goodTillDate': 0, 'updateTime': 1758707640628}
```

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

