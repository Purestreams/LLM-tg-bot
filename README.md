# Telegram Chat Bot

This is a Telegram chat bot built using Python and the `python-telegram-bot` library. The bot uses a text generation model from the `transformers` library to generate responses.

## To do list
- allow replying message and message chain
- create more roles

## Features

- Responds to the `/start` command with a welcome message.
- Responds to the `/chat` command with generated text based on user input.
- Uses a pre-trained text generation model to generate responses.

## Requirements

- Python 3.7+
- `python-telegram-bot`
- `torch`
- `transformers`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Purestreams/LLM-tg-bot.git
    cd LLM-tg-bot
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip3 install -r requirements.txt
    ```

4. Replace `#add your secret!` in `bot.py` with your actual Telegram bot token.

## Usage

1. Run the bot:

    ```sh
    python3 bot.py
    ```

2. Start a chat with your bot on Telegram and use the `/start` and `/chat` commands.

## File Structure

- `bot.py`: Main script containing the bot logic.
- `requirements.txt`: List of required Python packages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.