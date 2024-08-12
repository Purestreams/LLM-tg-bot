import logging
from telegram import Update
from telegram.ext import Application, filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import torch
import transformers
import threading
import queue
import asyncio
import time


# Initialize the lock
process_lock = threading.Lock()

task_queue = queue.Queue()

model_id = "aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

def validate_input(input):
    if input == "":
        return False
    if input.isspace():
        return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input = update.message.text
    if not validate_input(update.message.text):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a valid message!")
        return
    
    if input.startswith("/chat "):
        input = input.replace("/chat ", "")
        type = "catgirl"
    elif input.startswith("/chat@Chat_Mio_bot "):
        input = input.replace("/chat@Chat_Mio_bot ", "")
        type = "catgirl"
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a valid message!")
        return

    worker_thread = threading.Thread(target=process_chat_worker)
    if not worker_thread.is_alive():
        worker_thread.start()

    task_queue.put({"update": update, "input": input, "context": context, "type": type})

def process_chat_worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        
        with process_lock:
            asyncio.run(process_chat(task))
        task_queue.task_done()

async def process_chat(task):
    update = task["update"]
    input = task["input"]
    context = task["context"]
    type = task["type"]

    if type == "catgirl":
        mesage_template = [
            {"role": "system", "content": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible."},
            {'role': 'user', 'content': 'Who are you?'},
            {'role': 'assistant', 'content': 'My name is Mio. I am a helpful asistant.'},
        ]

    messages = mesage_template.copy()

    messages.append({'role': 'user', 'content': input})

    start_time = time.time()

    outputs = pipeline(
        messages,
        max_new_tokens=192,
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    generated_text = outputs[0]["generated_text"][-1]
    print("AI: ", generated_text, "Time: ", elapsed_time)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text["content"])
    #messages.append(generated_text)

        




def main():
    app = Application.builder().token('#add your secret!').build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("chat", chat))

    app.run_polling()

if __name__ == "__main__":
    main()
