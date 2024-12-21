import requests
import random

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Data retrieved with response code: {response}")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve Data with response code: {response}")
        print(f"Please double check your pokemon name.")

pokemon_name = "pikachu"
# pokemon_name = input("Enter the name of a Pokemon: ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")

    abilities = pokemon_info['abilities']   
    ability_names = [ability['ability']['name'] for ability in abilities] 
    print("Abilities:", ", ".join(ability_names))
    random_ability = random.choice(abilities)['ability']['name']
    print(f"Random Ability: {random_ability}")


