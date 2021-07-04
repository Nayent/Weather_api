from models import Weather, db

import requests


def percent(value):
    return round((value/167)*100, 2)
    

def get_data(response):
    city_id = response.get('id')

    kelvin = response.get('main',{}).get('temp')

    celcius = round(kelvin - 273.15, 2)

    humidity = response.get('main', {}).get('humidity')

    data = {
        'city_id': city_id,
        'temperature': celcius,
        'humidity': humidity
    }

    return data
    

def commit_psql(id, date, full_data):
        new_data = Weather(id, date, full_data)
        db.session.add(new_data)
        db.session.commit()