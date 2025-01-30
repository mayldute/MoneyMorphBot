import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    """Handle /start and /help commands"""
    text = f'Чтобы начать работу введите комманду боту в следующем формате:\n<имя вылюты>\
<в какyю валюту перевести>\
<количество валюты>\nУвидить все доступные валюты: /values'
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    
    for key in keys.keys():
        text = '\n'.join((text, key, ))
        
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    """Handle user's input"""
    try:
        values = message.text.split(' ')
        
        if len(values) != 3:
            raise APIException('Некорректное количество параметров. Повторите попытку ввода.')
            
        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось обработать команду. \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)
    
bot.polling()