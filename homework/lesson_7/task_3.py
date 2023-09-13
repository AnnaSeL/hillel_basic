import requests
import datetime


def get_forecast_requests(city, days):
    """Get forecast from the web page"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    API_KEY = f"f9ada9efec6a3934dad5f30068fdcbb8"
    API_URL = f"http://api.openweathermap.org/data/2.5/forecast/daily"
    params = {
        "q": city,
        "cnt": days,
        "appid": API_KEY
    }
    result = requests.get(API_URL, params=params, headers=headers)
    # result = requests.get(f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8',headers=headers)
    return result.json()


def save_to_file(city, days):
    """Saves data to txt file"""
    data = get_forecast_requests(city, days)
    with open(f"{datetime.datetime.now().strftime('%d-%m-%Y')}-{city}-{days}-days-weather-forecast.txt", "w+") as file:
        file.write("Дата Температура вдень Температура вночі\n")
        for forecast in data["list"]:
            date = datetime.datetime.fromtimestamp(forecast["dt"]).strftime("%d-%m-%Y")
            day_temp = forecast["temp"]["day"]
            night_temp = forecast["temp"]["night"]
            file.write(f"{date} {day_temp:.2f} {night_temp:.2f}\n")
        print(file.read())
    file.close()
    print_data()

def print_data():
    with open(f"{datetime.datetime.now().strftime('%d-%m-%Y')}-{city}-{days}-days-weather-forecast.txt", 'r') as f:
        content = f.read()
    print(content)


city = input("Enter city: ")
days = input("Enter amount of days: ")
save_to_file(city, days)
