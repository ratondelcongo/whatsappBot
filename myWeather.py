import pyowm

owm = pyowm.OWM('99ea3d5f5ce2b90174b5a525a31a8124')
observation = owm.weather_at_place('Lima,PE')
w = observation.get_weather()


def get_temp():
    temp = w.get_temperature('celsius')
    tempStr = 'Temp: ' + str(temp['temp']) + '°C  ' + \
        str(temp['temp_max']) + '/' + str(temp['temp_min'])
    return tempStr


def get_hum():
    hum = w.get_humidity()
    humStr = 'Humedad: ' + str(hum) + '%'
    return humStr
