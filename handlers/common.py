import os
from datetime import datetime

def save_image(image, prefix="image"):
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{prefix}_{timestamp}.png"
    image.save(filename)
    return filename

def send_image(bot, chat_id, image, caption=""):
    filename = save_image(image)
    with open(filename, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption)
    os.remove(filename)
