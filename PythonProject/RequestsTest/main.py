import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'da527c221a10e45d40f00b3f73bd9420'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 100
}
body_change = {
    "pokemon_id": "72065",
    "name": "Чипс"
}

body_add = {
    "pokemon_id": "72065"
}

'''requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)

print(response.text)'''

'''requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
response_change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change)

print(response_change.text)'''

requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)

print(response_add.text)