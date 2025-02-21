import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

keys = {
    'dollar': 'USD',
    'euro': 'EUR',
    'ruble': 'RUB'
}
