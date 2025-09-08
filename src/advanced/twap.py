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
    import sys

    if len(sys.argv) != 6:
        print("Usage: python twap.py SYMBOL SIDE TOTAL_QUANTITY NUM_SLICES INTERVAL_SECONDS")
        print("Example: python twap.py BTCUSDT BUY 0.01 5 60")
        sys.exit(1)

    symbol, side = sys.argv[1], sys.argv[2].upper()
    total_quantity, num_slices, interval_seconds = float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])

    API_KEY = "6fb8c22049dcaf1906093a75f421029449969dcb85391df8e9271d8fe1e3b227"
    API_SECRET = "00cde179d8253511429a0207defc11712be7fa729c124c8999776c6c93eabcfb"

    bot = TWAPBot(API_KEY, API_SECRET, testnet=True)
    bot.place_twap_order(symbol, side, total_quantity, num_slices, interval_seconds)


if __name__ == "__main__":
    main()

