
# 🖼️ Telegram Bot for Logo, Image, and Company Idea Generation

This project is a **Telegram bot** that uses Hugging Face AI models to generate custom logos, random logos, custom images, and fictional company ideas with descriptions and logos. It provides an engaging, creative experience for users right within Telegram.

---

## 🚀 Features

- **Custom Logo Generation**: Users can describe a logo, and the bot generates it based on their input.
- **Random Logo Generation**: Generates a random logo with a fictional company name.
- **Custom Image Generation**: Generates an image based on the user's description.
- **Fictional Company Ideas**: 
  - Generates a creative company name.
  - Creates a logo for the company.
  - Produces a brief description of the fictional company.

---

## 🛠️ Technologies Used

- **[Python](https://www.python.org/)**: The programming language used for the bot.
- **[Telebot](https://pypi.org/project/pyTelegramBotAPI/)**: Telegram Bot API library for interaction with users.
- **[Hugging Face Hub](https://huggingface.co/)**: For leveraging AI models to generate text and images.
- **Torch**: Backend library used by Hugging Face models.
- **Telegram Bot API**: For user communication.

---

## 📝 Prerequisites

Before you begin, ensure you have the following installed:

1. Python 3.8 or higher
2. A Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather)
3. An account on [Hugging Face](https://huggingface.co/) with API access.

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/b0lbas/aibot.git
   cd aibot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your credentials:**
   - Create a `.env` file in the root directory to securely store your tokens (optional).
   - Or edit the `config.py` file to directly input the following:
     - Telegram bot token
     - Hugging Face model and API token.

---

## 🏃‍♂️ Running the Bot

Start the bot with:

```bash
python bot.py
```

The bot will begin polling messages from Telegram users.

---

## 📖 How to Use

1. Add your bot to Telegram and send `/start` or `/help` to display the main menu.
2. Select one of the following options:
   - **Get Custom Logo**: Provide a description for your desired logo.
   - **Random Logo**: Instantly get a random logo with a fictional company name.
   - **Get Custom Image**: Describe an image you want to generate.
   - **Get a Company Idea**: Receive a unique company name, logo, and description.
3. The bot will process your request and respond with the generated content.

---

## 🗂️ Project Structure

```
project/
│
├── bot.py                 # Main file to run the bot
├── handlers/
│   ├── __init__.py        # Package initialization
│   ├── common.py          # Common helper functions
│   ├── logo_handler.py    # Logo generation logic
│   ├── image_handler.py   # Image generation logic
│   └── company_handler.py # Company idea generation logic
├── keyboards/
│   ├── __init__.py        # Package initialization
│   └── main_menu.py       # Telegram keyboard logic
├── config.py              # Configuration file for API keys and tokens
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

---

## 🌟 Acknowledgments

- Thanks to [Hugging Face](https://huggingface.co/) for providing incredible AI tools.
- Telegram Bot API for enabling easy bot interaction.

---

## 📧 Contact

For any inquiries or issues, please contact **[vladislav@bolbas.dev](mailto:vladislav@bolbas.dev)**.
