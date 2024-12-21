import requests

base_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="
base_im_url = "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player="
base_hcim_url = "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player="

def get_player_info(name, gamemode):
    if gamemode == "normal":
        url = f"{base_url}{name}"
    elif gamemode == "im":
        url = f"{base_im_url}{name}"
    else:
        url = f"{base_hcim_url}{name}"
    

    response = requests.get(url)

    if response.status_code == 200:
        print(player_name)
        player_data = response.text.strip()

        categories = ["Overall", "Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer", "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction"]
        player_data_lines = player_data.split('\n')
        for i in range(len(categories)): 
            category = categories[i]
            data_values = player_data_lines[i].split(',')
            rank, level, experience = data_values
            print(f"{category}: Rank = {rank}, Level = {level}, Experience = {experience}")

    else:
        print(f"Failed to retrieve data with response code: {response}")
        print(f"Please double-check your player name.")

player_name = input("Enter the player name: ")
game_mode = input("Enter the game mode: normal, im, hcim: ").lower()
valid_game_modes = ["normal", "im", "hcim"] 
if game_mode not in valid_game_modes: 
    print("Invalid game mode. Please enter one of the following: normal, im, hcim.") 
else: 
    get_player_info(player_name, game_mode)
