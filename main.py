import requests


YANDEX_SPEECHKIT_URL = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
YANDEX_SPEECHKIT_TOKEN = ''


def get_speech_from_text(text: str) -> bytes:
    """
    Синтезированный текст. По возможности используем кешированные данные.
    """
    headers = {
        'Authorization': f'Api-Key {YANDEX_SPEECHKIT_TOKEN}'
    }
    data = {
        'text': text,
        'lang': 'ru-RU',
        'speed': 0.9,  # чуть замедлим текст для лучшего восприятия
        'voice': 'alena',   # премиум
        # 'voice': 'filipp',   # премиум
        # 'voice': 'ermil',
        'emotion': 'good',
        'format': 'oggopus',
    }
    response = requests.post(url=YANDEX_SPEECHKIT_URL, headers=headers, data=data)
    response.raise_for_status()

    return response.content


audio_content = get_speech_from_text('Здравствуй, мамочка родная!')

f = open('audio.ogg', 'wb')
f.write(audio_content)
f.close()
