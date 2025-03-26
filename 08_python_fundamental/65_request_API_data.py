# How to connect to API data using Python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Error")

pokemon_name = "Typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: # if pokemon_info is True
    print(f"{pokemon_info['name']}")
    print(f"{pokemon_info['id']}")
    print(f"{pokemon_info['height']}")
    print(f"{pokemon_info['weight']}")