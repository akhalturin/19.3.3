import requests
import json

BASE_URL = 'https://petstore.swagger.io/v2'

new_pet = {
    "id": 97555545,
    "category": {
        "id": 1,
        "name": "Tom"
    },
    "name": "cat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 2,
            "name": "Jonny"
        }
    ],
    "status": "available"
}

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}


res = requests.post(f'{BASE_URL}/pet', headers=headers, data=json.dumps(new_pet, ensure_ascii=False))
print(res.json())
print(res.status_code)
print(res.text)
print(type(res.json()))


BASE_URL = 'https://petstore.swagger.io/v2'

id_new_pet = 97555545
headers1 = {'accept': 'application/json', 'Content-Type': 'application/json'}

res1 = requests.get(f'{BASE_URL}/pet/{id_new_pet}', headers=headers1, data=json.dumps(id_new_pet, ensure_ascii=False))

print(res1.json())
print(res1.status_code)
print(res1.text)
print(type(res1.json()))


BASE_URL = 'https://petstore.swagger.io/v2'

headers2 = {'accept': 'application/json', 'Content-Type': 'application/json'}

update_new_pet = {
    "id": 97555545,
    "category": {
        "id": 1,
        "name": "Sunny"
    },
    "name": "cat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 2,
            "name": "Vally"
        }
    ],
    "status": "sold"
}

res2 = requests.put(f'{BASE_URL}/pet', headers=headers2, data=json.dumps(update_new_pet, ensure_ascii=False))

print(res2.json())
print(res2.status_code)
print(res2.text)
print(type(res2.json()))


BASE_URL = 'https://petstore.swagger.io/v2'

id_new_pet = 97555545
headers3 = {'accept': 'application/json', 'Content-Type': 'application/json'}

res3 = requests.delete(f'{BASE_URL}/pet/{id_new_pet}', headers=headers3)

print(res3.json())
print(res3.status_code)
print(res3.text)
print(type(res3.json()))