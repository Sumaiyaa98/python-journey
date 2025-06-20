from api_keys import weather_api_key
import requests

def weather_app(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        raise Exception("City not found. Please check the spelling or try another city.")

    name = data["name"]
    weather_des = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return name, weather_des, temp, humidity

def main():
    city_name = input("Enter city name: ").lower()
    try:
        name, weather_des, temp, humidity = weather_app(city_name)
        print(f"\n📍 City: {name}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌤️ Description: {weather_des}")
        print(f"💧 Humidity: {humidity}%")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
