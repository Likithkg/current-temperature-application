import geocoder
import pyowm

def get_current_location():
    location = geocoder.ipinfo('me')
    if location.ok:
        return location.latlng
    else:
        return None

def get_current_temparature(latitude, longitude, apiKey):
    owm = pyowm.OWM(apiKey)
    try:
        mngr = owm.weather_manager()
        observation = mngr.weather_at_coords(latitude, longitude)
        weather = observation.get_weather()
        temperatuer = weather.get_temperature('celcius')['temp']
        return temperatuer
    except pyowm.commons.exceptions.NotFoundError as e:
        return None

current_location = get_current_location()
apiKey = '11c00b57eb40ee7abc17d4a1977d58ad'
if current_location:
    latitude, longitude = current_location
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    temperature = get_current_temparature(latitude, longitude, apiKey)
    if temperature is not None:
        print(f"Temperature in  Celsius: {temperature}°C")
else:
    print("unsucess")



