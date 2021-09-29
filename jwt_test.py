import jwt
payload_data = {
    "id": "001",
    "name": "rengoku",
    "age": 20,
    "gender": "boy"
}

token = jwt.encode(
    payload=payload_data,
    key='my_secret'
)
token = token+'K'
print(jwt.decode(token,'my_secret',algorithms=['HS256']))