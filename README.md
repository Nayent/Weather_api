# Weather_api

## How to run

To start the application run the following command:
```bash
python3 main.py
```

After this, the server will be running on http://127.0.0.1:5000.

### GET request

To make GET request run:
```bash
curl http://127.0.0.1:5000/?id=1
```

Passing ID as INTEGER

Or use Postman
![alt text](https://github.com/nayent/images/blob/main/postman.png?raw=true)

If the id exists, it will return the percentage for that id.

![alt text](https://github.com/nayent/images/blob/main/get_id.png?raw=true)

If does not exists, it will return an error message.

![alt text](https://github.com/nayent/images/blob/main/get_id_error.png?raw=true)

### POST request

To make POST request run:
```bash
curl -X POST http://127.0.0.1:5000/?id=1
```

Or in Postman

![alt text](https://github.com/nayent/images/blob/main/post_postman.png?raw=true)

If the id already exists, ir will return an error message.

![alt text](https://github.com/nayent/images/blob/main/postman_post.png?raw=true)

If the id does not exist, will make the request to the WeatherAPI, and after completed, will return a message to show that is done.

![alt text](https://github.com/nayent/images/blob/main/post_complete.png?raw=true)

When POST request is made, the data is collect from WeatherAPI and saved on postgreSQL database, using the following schema.

![alt text](https://github.com/nayent/images/blob/main/postgresql.png?raw=true)
