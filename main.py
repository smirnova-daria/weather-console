import requests

API_KEY = 'fd85cfdc7442ada7956eea08fb30064a'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'
LANG = 'ru'
FILE_EXCEL = 'weather.xlsx'


def get_weather(city):
    params = {
        'appid': API_KEY,
        'units': UNITS,
        'lang': LANG,
        'q': city,
    }
    try:
        r = requests.get(API_URL, params=params)
        return r.json()
    except:
        return {'cod': 0, 'message': 'Не удалось получить данные'}


print('*' * 70)
print("""o(*￣▽￣*)ブ Привет
Чтобы получить прогноз погоды, напиши название города
Чтобы выйти, нажми Enter
🪄🌤️🌧️❄️🌈""")
print('*' * 70)

while True:
    q = input("Город: ")
    if not q:
        print("👋Буду ждать тебя снова")
        break
    else:
        weather = get_weather(q)
        print(weather)
