import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'da527c221a10e45d40f00b3f73bd9420'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '8144'

def test_status():
    response = requests.get(url = f'{URL}/trainers',headers = HEADER, params = {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_name_trainer ():
    response_name = requests.get(url = f'{URL}/trainers',headers = HEADER, params = {'trainer_id' : TRAINER_ID} )
    assert response_name.json() ['data'] [0] ['trainer_name'] == 'Супер Шеф'