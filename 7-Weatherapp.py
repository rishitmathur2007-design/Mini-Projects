import requests
import configparser
config = configparser.ConfigParser()
config_file="wether_config.ini"
config.read(config_file)
api_key=config['Default']['api']
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
def getwether(city):

    result=requests.get(url.format(city,api_key))
    if result:
        data=result.json()
        city=data['name']
        country=data['sys']["country"]
        humidity=data["main"]["humidity"]
        tempe=data["main"]["temp"]
        weather1=data['weather'][0]['main']
        print("--------Weather Report--------")
        print("City:",city)
        print("Country:",country)
        print("Temperature:",tempe,"C")
        print("Humidity:",humidity,"%")
        print("Weather:",weather1)
    else:
        print("No Content Found")
city_nm=input("Enter City Name:")
getwether(city_nm)