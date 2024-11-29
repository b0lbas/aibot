import telebot
from configfile import TOKEN
from keyboards.main_menu import main_menu
from handlers.logo_handler import generate_logo, generate_random_logo
from handlers.image_handler import generate_custom_image
from handlers.company_handler import generate_company_idea

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text in ['/help', '/start', 'Return to main page']:
        markup = main_menu()
        bot.send_message(message.chat.id, "Choose an option from below", reply_markup=markup)
    elif message.text == 'Get custom logo':
        msg = bot.send_message(message.chat.id, "Describe your logo")
        bot.register_next_step_handler(msg, generate_logo, bot)
    elif message.text == 'Random logo':
        generate_random_logo(bot, message.chat.id)
    elif message.text == 'Get custom image':
        msg = bot.send_message(message.chat.id, "Describe your image")
        bot.register_next_step_handler(msg, generate_custom_image, bot)
    elif message.text == 'Get a company idea 🟣':
        generate_company_idea(bot, message.chat.id)

if __name__ == "__main__":
    bot.polling(none_stop=True)
