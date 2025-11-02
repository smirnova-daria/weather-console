from funcs import get_weather, get_weather_desc, save_excel

print('*' * 50)
print("""o(*￣▽￣*)ブ Привет
Чтобы получить прогноз погоды, напиши название города
Чтобы выйти, нажми Enter
🪄🌤️🌧️❄️🌈""")

while True:
    print('*' * 50)
    q = input("Город: ")
    if not q:
        print("👋Буду ждать тебя снова")
        break
    else:
        weather = get_weather(q)
        print(get_weather_desc(weather))
        save_excel(weather)
