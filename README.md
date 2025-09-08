# Binance Futures Order Bot

## Overview

This project is a modular, CLI-based trading bot designed for Binance USDT-M Futures Testnet. It supports essential order types such as **Market Orders**, **Limit Orders**, and advanced strategies including **OCO (One-Cancels-the-Other)** and **TWAP (Time-Weighted Average Price)**. The bot interfaces with Binance Futures Testnet API via the official `python-binance` client.

## Features

- Interactive command-line input for placing various types of orders.
- Modular Python scripts for different order types:
  - Market orders
  - Limit orders
  - OCO advanced orders
  - TWAP order execution strategy
- Robust logging of orders, responses, and errors in a `bot.log` file.
- Designed for safe testing on Binance Futures Testnet environment.

## Project Structure

main/
├── src/
│ ├── market_orders.py
│ ├── limit_orders.py
│ └── advanced/
│ ├── oco.py
│ └── twap.py
├── bot.log 
├── README.md 
└── report.pdf 

## Setup & Installation

1. **Prerequisites:**

   - Python 3.7 or newer installed
   - `python-binance` library installed via pip

2. **Get Binance Futures Testnet API Keys:**

- Register and obtain your API key and secret at [Binance Futures Testnet](https://testnet.binancefuture.com/en/futures/BTCUSDT).

3. **Configure API Keys:**

- Open each script inside `src/` and `src/advanced/`.
- Replace the placeholder variables with your API keys:


## Usage

Run the appropriate script from the terminal depending on desired order type.

### Market Order
You will be prompted to enter:

- Trading symbol (e.g., BTCUSDT)
- Side (BUY or SELL)
- Quantity

### Limit Order
Prompts include:

- Trading symbol
- Side
- Quantity
- Limit price

### OCO Order (Advanced)
Prompts include:

- Trading symbol
- Side
- Quantity
- Take profit price
- Stop price
- Stop limit price

### TWAP Order (Advanced)

Prompts include:

- Trading symbol
- Side
- Total quantity
- Number of slices
- Interval between slices (seconds)
  
## Logs and Monitoring
- All order-related activities, including API responses and errors, are logged with timestamps in `bot.log`.
- The log file can be found in the project root directory.
- Review this file for auditing and troubleshooting.
  
## Important Notes
- This bot is intended **only for Binance Futures Testnet** and NOT for live trading without thorough testing and risk controls.
- OCO automatic cancellation is not implemented; manual monitoring needed.
- Use Python 3.7+ for compatibility.
- Always safeguard your API keys and never share them publicly.




