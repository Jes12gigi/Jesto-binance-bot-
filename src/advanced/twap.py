from binance.client import Client
import logging
import time

class TWAPBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi' if testnet else self.client.FUTURES_URL
        logging.basicConfig(filename='../../bot.log', level=logging.INFO,
                            format='%(asctime)s : %(levelname)s : %(message)s')

    def place_twap_order(self, symbol, side, total_quantity, num_slices, interval_seconds):
        slice_qty = total_quantity / num_slices
        logging.info(f"Starting TWAP: {total_quantity} {symbol} in {num_slices} slices")
        for i in range(num_slices):
            try:
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=round(slice_qty, 6)
                )
                logging.info(f"TWAP slice {i+1}/{num_slices} placed: {order}")
                print(f"TWAP slice {i+1}/{num_slices} placed")
            except Exception as e:
                logging.error(f"Failed to place TWAP slice {i+1}: {e}")
                print(f"Failed to place TWAP slice {i+1}: {e}")
            if i < num_slices - 1:
                time.sleep(interval_seconds)
        logging.info("Completed TWAP order")

def main():
    print("TWAP Order Placement")
    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY or SELL): ").strip().upper()
    total_qty_input = input("Enter total quantity: ").strip()
    num_slices_input = input("Enter number of slices: ").strip()
    interval_input = input("Enter interval in seconds: ").strip()

    try:
        total_quantity = float(total_qty_input)
        num_slices = int(num_slices_input)
        interval_seconds = int(interval_input)
    except ValueError:
        print("Invalid input. Quantity, slices, and interval must be numbers.")
        return

    API_KEY = "6fb8c22049dcaf1906093a75f421029449969dcb85391df8e9271d8fe1e3b227"
    API_SECRET = "00cde179d8253511429a0207defc11712be7fa729c124c8999776c6c93eabcfb"

    bot = TWAPBot(API_KEY, API_SECRET, testnet=True)
    bot.place_twap_order(symbol, side, total_quantity, num_slices, interval_seconds)

if __name__ == "__main__":
    main()
