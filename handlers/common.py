# handlers/common.py

import os
from datetime import datetime

def save_image(image, prefix="image"):
    """Save an image to a temporary file and return its filename."""
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{prefix}_{timestamp}.png"
    image.save(filename)
    return filename

def send_image(bot, chat_id, image, caption=""):
    """Send an image to the user and delete it locally."""
    filename = save_image(image)
    with open(filename, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption)
    os.remove(filename)