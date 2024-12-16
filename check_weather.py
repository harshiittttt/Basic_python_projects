import requests
def check_weather(city,api_key):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {
        'key':api_key,
        'q':city,
        'aqi': "no"
    }
    try:
     response = requests.get(base_url, params)
     response.raise_for_status()
     weather_data = response.json()
     city = weather_data["location"]["name"]
     region = weather_data["location"]["region"]
     country = weather_data["location"]["country"]
     temperature = weather_data["current"]["temp_c"]
     condition = weather_data["current"]["condition"]["text"]
     humidity = weather_data["current"]["humidity"]
     wind_speed = weather_data["current"]["wind_kph"]
     return (f"Weather in {city}, {region}, {country}:\n"
             f"Temperature: {temperature}°C\n"
             f"Condition: {condition}\n"
             f"Humidity: {humidity}%\n"
             f"Wind Speed: {wind_speed} km/h")
    except:
        print("Something went wrong or invalid api or City name")
def forecasting(city,apikey,days):
    base_url = 'http://api.weatherapi.com/v1/forecast.json'
    params = {
        'key':apikey,
        'q':city,
        'aqi': "no",
        'days':days
    }
    try:
        response = requests.get(base_url, params)
        response.raise_for_status()
        forecase_data= response.json()
        city = forecase_data["location"]["name"]
        region = forecase_data["location"]["region"]
        country = forecase_data["location"]["country"]
        forecast = f"Weather forecast for {city}, {region}, {country}:\n"
        for day in forecase_data["forecast"]["forecastday"]:
            date = day["date"]
            max_temp = day["day"]["maxtemp_c"]
            min_temp = day["day"]["mintemp_c"]
            condition = day["day"]["condition"]["text"]
            avg_temp = day["day"]["avgtemp_c"]
            forecast += (f"\nDate: {date}\n"
                         f"Max Temp: {max_temp}°C\n"
                         f"Min Temp: {min_temp}°C\n"
                         f"Avg temp: {avg_temp}\n"
                         f"Condition: {condition}\n"
                         )

        return forecast

    except:
         print("something went wrong or invalid api or City name")


def main():
    key = "1001b99881aa413e81a190637241612"
    sehar = input("Please enter the city for which you want to get the weather report\n")

    while True:
        user_choice = int(input("1. CURRENT STATUS\n2. FORECAST\n"))

        if user_choice == 1:
            weather_report = check_weather(sehar, key)
            print(weather_report)
        elif user_choice == 2:
            numberof_days = int(input(
                "Please enter the number of days for which you want to get the weather report (should be less than 10)\n"))
            forecast_report = forecasting(sehar, key, numberof_days)
            print(forecast_report)
        else:
            print("Invalid choice! Please select either 1 or 2.")


        continue_choice = input("Do you want to check another report? (yes/no)\n").strip().lower()
        if continue_choice != 'yes':
            break


main()
