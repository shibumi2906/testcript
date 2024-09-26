import os
from pybit.unified_trading import HTTP
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Инициализация сессии Bybit
session = HTTP(
    demo=True,
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_SECRET_KEY")
)
