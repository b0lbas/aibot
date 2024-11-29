from huggingface_hub import InferenceClient
from handlers.common import send_image
from configfile import HF_MODEL, HF_TOKEN
from datetime import datetime

image_client = InferenceClient(HF_MODEL, token=HF_TOKEN)

def generate_logo(message, bot):
    bot.send_message(message.chat.id, "Your custom logo is being generated, please wait...")
    prompt = f"Generate a logo with these exact instructions: {message.text}"
    image = image_client.text_to_image(prompt)
    send_image(bot, message.chat.id, image)

def generate_random_logo(bot, chat_id):
    timestamp = datetime.now().strftime("%H%M%S")
    bot.send_message(chat_id, "Your random logo is being generated, please wait...")
    prompt = f"Generate a random logo with a random company name in it (unrelated: {timestamp})"
    image = image_client.text_to_image(prompt)
    send_image(bot, chat_id, image)
