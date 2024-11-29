# handlers/company_handler.py

from huggingface_hub import InferenceClient
from handlers.common import send_image
from configfile import HF_INSTRUCTION_MODEL, HF_MODEL, HF_TOKEN
from datetime import datetime

# Initialize clients
image_client = InferenceClient(HF_MODEL, token=HF_TOKEN)
chat_client = InferenceClient(api_key=HF_TOKEN)

def generate_text(model, messages, max_tokens=500):
    """Generate text using the inference client."""
    stream = chat_client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        stream=True
    )
    result = "".join(chunk.choices[0].delta.content for chunk in stream)
    return result.strip()

def generate_company_idea(bot, chat_id):
    """Generate a company name, logo, and description."""
    bot.send_message(chat_id, "Please wait...")
    current_time = datetime.now().strftime("%H%M%S")

    # Generate company name
    name_prompt = [{"role": "user", "content": f"Generate a company name. Current time: {current_time}"}]
    company_name = generate_text(HF_INSTRUCTION_MODEL, name_prompt)

    # Generate company logo
    prompt = f"Generate a logo for a company called {company_name}"
    image = image_client.text_to_image(prompt)

    # Generate company description
    description_prompt = [
        {"role": "system", "content": "Generate a brief description of a fictional company. Max 300 characters."},
        {"role": "user", "content": f"Create a brief description for company {company_name}."}
    ]
    description = generate_text(HF_INSTRUCTION_MODEL, description_prompt)

    # Combine results and send to user
    caption = f"❗️{company_name}❗️\n\n{description}"
    send_image(bot, chat_id, image, caption)