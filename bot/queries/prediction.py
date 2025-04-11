import os
import json
import torch
import requests
from PIL import Image
from dotenv import load_dotenv
from transformers import BlipProcessor, BlipForConditionalGeneration

load_dotenv()

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
YANDEX_ID_CATALOG = os.environ["YANDEX_ID_CATALOG"]
YANDEX_API_KEY = os.environ["YANDEX_API_KEY"]


name_model = "abhijit2111/Pic2Story"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
processor = BlipProcessor.from_pretrained(name_model)
model = BlipForConditionalGeneration.from_pretrained(name_model).to(device)


# Генерация URL адресов загруженных изображений в TG
def tg_photo_url(photo_file_id: str):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/getFile?file_id={photo_file_id}"
    file_path = requests.get(url).json()["result"]["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TG_BOT_TOKEN}/{file_path}"
    return photo_url


def prediction_captions(photo_url: dict):
    captions = []

    for image in photo_url:
        image = Image.open(requests.get(tg_photo_url(image), stream=True).raw)
        inputs = processor(image, return_tensors="pt").to(device)
        out = model.generate(**inputs)
        captions.append(processor.decode(out[0], skip_special_tokens=True))
    return captions


def prediction_history(message: str):
    prompt = {
        "modelUri": f"gpt://{YANDEX_ID_CATALOG}/yandexgpt/latest",
        "completionOptions": {"stream": False, "temperature": 0.6, "maxTokens": "2000"},
        "messages": [
            {
                "role": "system",
                "text": "Ты русский писатель детских рассказов. Всегда возвращаешь текст только на русском."
                "В тексте запрещено использовать: фотография, изображение, затем, фото, арафед, arafed, развернутое, описание, *, #",
            },
            {
                "role": "user",
                "text": message,
            },
        ],
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {YANDEX_API_KEY}",
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = json.loads(response.text)

    return result["result"]["alternatives"][0]["message"]["text"]


def instructions_history(photo_captions, photo_description: str):
    setup_input = "Запрещено выводить примечания"
    message = f"""
            Напиши развернутое описание от первого лица происходящего на {len(photo_captions)} фотографиях объединив в сюжет.
            Подписи к фотографиям: {photo_captions}.
            Описание событий, происходящих на фотографиях: {photo_description}.
            Дополнительные требования: {setup_input}.
            """
    return message
