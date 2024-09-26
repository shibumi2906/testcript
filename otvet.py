import re
from pybit.unified_trading import HTTP

# Инициализация сессии Bybit (предполагается, что ключи API у вас уже есть)
api_key = 'ваш_api_key'
api_secret = 'ваш_secret_key'
session = HTTP(demo=True, api_key=api_key, api_secret=api_secret)

def extract_trade_data(message):
    # Пример регулярного выражения для поиска takeProfit и stopLoss в сообщении
    take_profit = re.search(r'takeProfit: (\d+)', message)
    stop_loss = re.search(r'stopLoss: (\d+)', message)

    if take_profit and stop_loss:
        return int(take_profit.group(1)), int(stop_loss.group(1))
    return None, None

def execute_trade(take_profit, stop_loss):
    try:
        order = session.place_active_order(
            symbol="BTCUSDT",
            side="Buy",  # Предполагаем покупку для примера
            order_type="Market",
            qty=0.01,  # Пример количества
            take_profit=take_profit,
            stop_loss=stop_loss,
            time_in_force="GoodTillCancel"
        )
        print(f"Открыт ордер: {order}")
    except Exception as e:
        print(f"Ошибка при открытии ордера: {e}")
