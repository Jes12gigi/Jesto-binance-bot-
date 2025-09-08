from binance.client import Client
import logging

class LimitOrderBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi' if testnet else self.client.FUTURES_URL
        logging.basicConfig(filename='../bot.log', level=logging.INFO,
                            format='%(asctime)s : %(levelname)s : %(message)s')

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f"Limit order placed: {order}")
            print(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit order failed: {e}")
            print(f"Limit order failed: {e}")
            return None

def main():
    print("Limit Order Placement")
    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY or SELL): ").strip().upper()
    quantity_input = input("Enter quantity: ").strip()
    price_input = input("Enter limit price: ").strip()

    try:
        quantity = float(quantity_input)
        price = float(price_input)
    except ValueError:
        print("Invalid quantity or price. Must be numbers.")
        return

    API_KEY = "6fb8c22049dcaf1906093a75f421029449969dcb85391df8e9271d8fe1e3b227"
    API_SECRET = "00cde179d8253511429a0207defc11712be7fa729c124c8999776c6c93eabcfb"

    bot = LimitOrderBot(API_KEY, API_SECRET, testnet=True)
    bot.place_limit_order(symbol, side, quantity, price)

if __name__ == "__main__":
    main()
