import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}