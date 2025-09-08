from binance.client import Client
import logging

class OCOOrderBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi' if testnet else self.client.FUTURES_URL
        logging.basicConfig(filename='../../bot.log', level=logging.INFO,
                            format='%(asctime)s : %(levelname)s : %(message)s')

    def place_oco_order(self, symbol, side, quantity, take_profit_price, stop_price, stop_limit_price):
        try:
            take_profit_side = "SELL" if side == "BUY" else "BUY"

            take_profit_order = self.client.futures_create_order(
                symbol=symbol,
                side=take_profit_side,
                type='LIMIT',
                quantity=quantity,
                price=take_profit_price,
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

        # Note: Cancellation logic between the two orders is not implemented here

def main():
    print("OCO Order Placement")
    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY or SELL): ").strip().upper()
    quantity_input = input("Enter quantity: ").strip()
    tp_price_input = input("Enter take profit price: ").strip()
    stop_price_input = input("Enter stop price: ").strip()
    stop_limit_price_input = input("Enter stop limit price: ").strip()

    try:
        quantity = float(quantity_input)
        take_profit_price = float(tp_price_input)
        stop_price = float(stop_price_input)
        stop_limit_price = float(stop_limit_price_input)
    except ValueError:
        print("Invalid input. Quantity and prices must be numbers.")
        return

    API_KEY = "6fb8c22049dcaf1906093a75f421029449969dcb85391df8e9271d8fe1e3b227"
    API_SECRET = "00cde179d8253511429a0207defc11712be7fa729c124c8999776c6c93eabcfb"

    bot = OCOOrderBot(API_KEY, API_SECRET, testnet=True)
    bot.place_oco_order(symbol, side, quantity, take_profit_price, stop_price, stop_limit_price)

if __name__ == "__main__":
    main()
