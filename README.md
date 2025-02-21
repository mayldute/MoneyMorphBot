# MoneyMorphBot

This project implements a Telegram bot for converting currencies using real-time exchange rates. The bot allows users to convert amounts between various cryptocurrencies and fiat currencies based on the current exchange rates.

## Features

The bot provides the following features:

- Converting an amount from one currency to another.
- Listing all available currencies for conversion.

## Technologies

- **Python** – Programming language used for the bot.
- **Telebot** – Python library for creating Telegram bots.
- **Requests** – Python library for making HTTP requests to the CryptoCompare API.
- **JSON** – Used to handle API responses.

## How to Deploy the Project

### Install Dependencies

To install the dependencies, run the command:
```sh
pip install -r requirements.txt
```

### Configure the Bot

Before starting the project, configure the necessary environment variables. Create a `.env` file with the following content:

```
API_KEY=<your_api_key>
BOT_TOKEN=<your_bot_token>
```

### Start the Bot

To start the bot, use the command:
```sh
python bot.py
```

## How to Use the Bot

- **Start the Bot**: Use the `/start` or `/help` commands to get instructions on how to use the bot.
- **Convert Currencies**: Send a message in the format: `<currency_from> <currency_to> <amount>`. For example, sending `BTC USD 1` will convert 1 Bitcoin (BTC) to USD based on the current exchange rate.
- **List Available Currencies**: Use the `/values` command to get a list of all supported currencies.

## Error Handling

- **Invalid Input Format**: If the user does not provide the correct format (e.g., missing parameters or wrong data types), the bot will respond with an error message like: `Incorrect number of parameters. Please try again.`
- **Invalid Currency**: If an unsupported or incorrect currency is provided, the bot will inform the user with an error like: `Failed to process currency <currency_name>!`
- **General Errors**: If any other error occurs during the process (e.g., network issues or API failures), the bot will return a generic error message: `Failed to process the command. <error_details>`
