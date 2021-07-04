# Weather_api

Save data for specific cities in JSON format into a postgresql database.
The data takes time to come and save, so there is the GET request, which returns how many percent has already been saved, considering that there are 167 cities to get on each request

## How to run

To start the application run the following command:
```bash
python3 main.py
```

After this, the server will be running on http://127.0.0.1:5000/

### GET request

To make GET request run:
```bash
curl http://127.0.0.1:5000/?id=1
```

Passing ID as INTEGER.

Or using Postman.

If the id exists, it will return the percentage for that id.

![alt text](https://github.com/nayent/images/blob/main/get_percent.png?raw=true)

If does not exists, it will return an error message.

![alt text](https://github.com/nayent/images/blob/main/get_id_exist.png?raw=true)

### POST request

To make POST request run:
```bash
curl -X POST http://127.0.0.1:5000/?id=1
```

Or in Postman

If the id already exists, ir will return an error message.

![alt text](https://github.com/nayent/images/blob/main/post_id_exist.png?raw=true)

If the id does not exist, will make the request to the WeatherAPI, and after completed, will return a message to show that is done.

![alt text](https://github.com/nayent/images/blob/main/post_done.png?raw=true)

When POST request is made, the data is collect from WeatherAPI and saved on postgreSQL database, using the following schema.

![alt text](https://github.com/nayent/images/blob/main/postgresql.png?raw=true)

## How to test

To run all tests just needed to run

```bash
python3 -m unittest -v
```
