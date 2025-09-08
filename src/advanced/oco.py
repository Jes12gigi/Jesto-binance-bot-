from binance.client import Client
import logging
import time
class OCOOrderBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi' if testnet else self.client.FUTURES_URL
        logging.basicConfig(filename='../../bot.log', level=logging.INFO,
                            format='%(asctime)s : %(levelname)s : %(message)s')

    def place_oco_order(self, symbol, side, quantity, price, stop_price, stop_limit_price):
        try:
            take_profit_side = "SELL" if side == "BUY" else "BUY"
            take_profit_order = self.client.futures_create_order(
                symbol=symbol,
                side=take_profit_side,
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f"Take profit order placed: {take_profit_order}")
            print(f"Take profit order placed: {take_profit_order}")
        except Exception as e:
            logging.error(f"Failed to place take profit order: {e}")
            print(f"Failed to place take profit order: {e}")
            return None
        try:
            stop_limit_order = self.client.futures_create_order(
                symbol=symbol,
                side=take_profit_side,
                type='STOP_LIMIT',
                quantity=quantity,
                price=stop_limit_price,
                stopPrice=stop_price,
                timeInForce='GTC'
            )
            logging.info(f"Stop limit order placed: {stop_limit_order}")
            print(f"Stop limit order placed: {stop_limit_order}")
        except Exception as e:
            logging.error(f"Failed to place stop limit order: {e}")
            print(f"Failed to place stop limit order: {e}")
            return None
        return take_profit_order, stop_limit_order
def main():
    import sys

    if len(sys.argv) != 7:
        print("Usage: python oco.py SYMBOL SIDE QUANTITY TAKE_PROFIT_PRICE STOP_PRICE STOP_LIMIT_PRICE")
        print("Example: python oco.py BTCUSDT BUY 0.001 120000 118000 117500")
        sys.exit(1)

    symbol, side, quantity, take_profit_price, stop_price, stop_limit_price = sys.argv[1], sys.argv[2].upper(), float(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
    take_profit_price = float(take_profit_price)
    stop_price = float(stop_price)
    stop_limit_price = float(stop_limit_price)

    API_KEY = "6fb8c22049dcaf1906093a75f421029449969dcb85391df8e9271d8fe1e3b227"
    API_SECRET = "00cde179d8253511429a0207defc11712be7fa729c124c8999776c6c93eabcfb"

    bot = OCOOrderBot(API_KEY, API_SECRET, testnet=True)
    bot.place_oco_order(symbol, side, quantity, take_profit_price, stop_price, stop_limit_price)


if __name__ == "__main__":
    main()

