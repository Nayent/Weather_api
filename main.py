from datetime import datetime
from flask import Flask, json, jsonify, request
from sqlalchemy import func

from models import Weather, app, db
from weather_data import city_ids, api_key
from lib import percent, get_data, commit_psql

import requests
import time


@app.route('/', methods=['GET', 'POST'])
def weather_api():
    if(request.method == 'GET'):
        post_data = request.args.get('id')

        if not post_data:
            return jsonify({'Error': 'Id is missing'})

        id = int(post_data)

        count = db.session.query(
            func.json_array_length(Weather.data).label('count_data')
        ).filter(Weather.id == id)

        count = [x.count_data for x in count]

        if len(count) > 0:
            perc = percent(count[0])
            return jsonify({'Percent': f'{perc}%'})
        else:
            return jsonify({'Error': f'There is no ID {id}'})
            

    elif request.method == 'POST':
        # Get data id
        post_data = request.args.get('id')

        if not post_data:
            return jsonify({'Error': 'Id is missing'})

        id = int(post_data)

        data_db = Weather.query.all()
        data_db = [data.id for data in data_db]
        
        if id in data_db:
            return jsonify({'Error': 'Id already exist'})

        full_data = []
        remains = 166

        date = str(datetime.now())[:19]

        # First commit psql
        commit_psql(id, date, full_data)

        for row in range(len(city_ids)):
            url = f'http://api.openweathermap.org/data/2.5/weather?id={city_ids[row]}&appid={api_key}'
            # time.sleep(5)

            response = requests.get(url).json()

            data = get_data(response)

            full_data.append(data)

            print('remain %d' % remains)
            remains -= 1

            # Update with new city data
            data_update = Weather.query.filter_by(id=id).update(dict(data=full_data))
            db.session.commit()

        return 'All Done'

    else:
        return jsonify({'Error': 'No method available'})

if __name__ == '__main__':
    app.run()