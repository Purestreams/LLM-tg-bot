# Telegram Chat Bot

This is a Telegram chat bot built using Python and the `python-telegram-bot` library. The bot uses a text generation model from the `transformers` library to generate responses.

## To do list
- allow replying message and message chain
- create more roles


## Features

- Responds to the `/start` command with a welcome message.
- Responds to the `/chat` command with generated text based on user input.
- Uses a pre-trained text generation model to generate responses.
- Utilizes the [DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored) model from Hugging Face for text generation.



## Requirements

- Python 3.7+
- `python-telegram-bot`
- `torch`
- `transformers`


Require at least 16GB of vram at default, test with Tesla P40.
```sh
Tue Aug 13 03:43:01 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.183.01             Driver Version: 535.183.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla P40                      On  | 00000000:01:00.0 Off |                  Off |
| N/A   51C    P0              54W / 250W |  16104MiB / 24576MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A       797      G   /usr/lib/xorg/Xorg                            4MiB |
|    0   N/A  N/A     12111      C   python3                                   16098MiB |
+---------------------------------------------------------------------------------------+
```

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