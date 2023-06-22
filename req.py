import requests

# GET запрос
res = requests.get("https://petstore.swagger.io/v2/pet/1")
print(res.status_code)
print(res.text)
print(res.json())

# POST запрос
new_pet = {
    "id": 1,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "kitty",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

res = requests.post("https://petstore.swagger.io/v2/pet", json=new_pet)
print(res.status_code)
print(res.text)
print(res.json())

# PUT запрос
updated_pet = {
    "id": 1,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie2",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

res = requests.put("https://petstore.swagger.io/v2/pet", json=updated_pet)
print(res.status_code)
print(res.text)
print(res.json())

# DELETE запрос
res = requests.delete("https://petstore.swagger.io/v2/pet/1")
print(res.status_code)
print(res.text)
print(res.json())



