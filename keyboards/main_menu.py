# keyboards/main_menu.py

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    """Create the main menu keyboard."""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Get custom logo'))
    markup.add(KeyboardButton('Random logo'))
    markup.add(KeyboardButton('Get custom image'))
    markup.add(KeyboardButton('Get a company idea 🟣'))
    return markup
