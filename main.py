from pokemon_generator import *

counts = 6
win = False
pokemon_info = get_pokemon_info(generate_fixed_number()) # Günün pokemonu

while counts > 0:
    guess = input(f"Günün pokemonunu tahmin edin ({counts} hakkınız kaldı.):")
    guessed_info = get_pokemon_info(str(guess))

    if guessed_info and pokemon_info:
        if guessed_info["name"] == pokemon_info["name"]:
            print(f"Name: {guessed_info["name"]} --> 🟢")
            win = True
        else:
            print(f"Name: {guessed_info["name"]} --> 🔴")
        
        if guessed_info["height"] == pokemon_info["height"]:
            print(f"Height: {guessed_info["height"]/10} meters --> 🟢")
        elif abs(guessed_info["height"] - pokemon_info["height"]) < 10:
            print(f"Height: {guessed_info["height"]/10} meters --> 🟡")
        else:
            print(f"Height: {guessed_info["height"]/10} meters --> 🔴")
        
        if guessed_info["weight"] == pokemon_info["weight"]:
            print(f"Weight: {guessed_info["weight"]/10} kilograms --> 🟢")
        elif abs(guessed_info["weight"] - pokemon_info["weight"]) < 10:
            print(f"Weight: {guessed_info["weight"]/10} kilograms --> 🟡")
        else:
            print(f"Weight: {guessed_info["weight"]/10} kilograms --> 🔴")

        if guessed_info["types"][0]["type"]["name"] == pokemon_info["types"][0]["type"]["name"]:
            print(f"Type: {guessed_info["types"][0]["type"]["name"]} --> 🟢")
        else:
            print(f"Type: {guessed_info["types"][0]["type"]["name"]} --> 🔴")
        
        if win == False:
            counts -=1
        else:
            break

if win == True:
    print(f"Bugünün Pokemon'unu {7-counts} tahminde buldunuz! 😄")
else:
    print("Bugünün Pokemonunu bulamadınız. 😔\nBugünün Pokemonu:")
    
    if pokemon_info:
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"ID: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]/10} meters")
        print(f"Weight: {pokemon_info["weight"]/10} kilograms")
        print(f"Type: {pokemon_info["types"][0]["type"]["name"].capitalize()}")
