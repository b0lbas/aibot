# handlers/image_handler.py

from huggingface_hub import InferenceClient
from handlers.common import send_image
from configfile import HF_MODEL, HF_TOKEN

# Initialize the image generation client
image_client = InferenceClient(HF_MODEL, token=HF_TOKEN)

def generate_custom_image(message, bot):
    bot.send_message(message.chat.id, "Your image is being generated, please wait...")
    prompt = message.text
    image = image_client.text_to_image(prompt)
    send_image(bot, message.chat.id, image)
