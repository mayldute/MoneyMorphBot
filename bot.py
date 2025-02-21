import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    """Handle /start and /help commands"""
    text = f'To start working, enter the command to the bot in the following format:\n<currency name>\
<currency to convert to>\
<amount of currency>\nTo see all available currencies: /values'
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    
    for key in keys.keys():
        text = '\n'.join((text, key, ))
        
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    """Handle user's input"""
    try:
        values = message.text.split(' ')
        
        if len(values) != 3:
            raise APIException('Incorrect number of parameters. Please try again.')
            
        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'User error.\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Failed to process the command. \n{e}')
    else:
        text = f'The price of {amount} {quote} in {base} is {total_base}'
        bot.send_message(message.chat.id, text)
    
bot.polling()
