**@MoneyMorphBot** is a Telegram bot for converting currencies using real-time exchange rates. It allows users to convert amounts between various cryptocurrencies (e.g., Bitcoin, Ethereum) based on their selected conversion rate.

**Features:**

Currency conversion: The bot allows you to convert an amount from one currency to another (e.g., BTC to USD).

**Supported commands:**

/start and /help: Provides a guide on how to use the bot.

/values: Displays all available currencies that can be converted.

Text input for currency conversion (e.g., "BTC USD 1" to convert 1 Bitcoin to USD).

**How to Use:**

Start the bot: Use the /start or /help commands to get instructions on how to use the bot.

Currency conversion: To convert currencies, send a message in the format:
<currency_from> <currency_to> <amount>

For example, sending BTC USD 1 will convert 1 Bitcoin (BTC) to USD based on the current exchange rate.

List available currencies: Use the /values command to get a list of all supported currencies.
Error Handling

Invalid input format: If the user does not provide the correct format (e.g., missing parameters or wrong data types), the bot will respond with an error message like:
Некорректное количество параметров. Повторите попытку ввода.

Invalid currency: If an unsupported or incorrect currency is provided, the bot will inform the user with an error like:
Не удалось обработать валюту <currency_name>!

General errors: If any other error occurs during the process (e.g., network issues or API failures), the bot will return a generic error message:
Не удалось обработать команду. <error_details>

**Technologies:**

Python: Programming language used for the bot.

Telebot: Python library for creating Telegram bots.

Requests: Python library for making HTTP requests to the CryptoCompare API.

JSON: Used to handle API responses.
