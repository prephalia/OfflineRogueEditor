import json, requests, random, os, time

class Rogue:
    def __init__(self) -> None:
        with open("./data/pokemon.json") as f:
            self.pokemon_id_by_name = json.loads(f.read())
        
        with open("./data/biomes.json") as f:
            self.biomes_by_id = json.loads(f.read())

        with open("./data/moves.json") as f:
            self.moves_by_id = json.loads(f.read())
        
        with open("./data/data.json") as f:
            self.extra_data = json.loads(f.read())
    
    def unlock_all_starters(self):

        with open("data_Guest.json") as f:
            data = json.loads(f.read())

        if not data:
            return None
        total_caught = 0
        total_seen = 0
        for entry in data["dexData"].keys():
            caught = random.randint(150, 250)
            seen = random.randint(150, 350)
            total_caught += caught
            total_seen += seen
            data["dexData"][entry] = {
                "$sa": 479,
                "$ca": 255,
                "$na": 67108862,
                "$s": seen,
                "$c": caught,
                "$hc": 0,
                "$i": [31, 31, 31, 31, 31, 31]
            }
            data["starterData"][entry] = {
                "$m": None,
                "$em": 15,
                "$x": caught + 20,
                "$a": 7,
                "$pa": 0,
                "$vr": 0
            }
            data["gameStats"]["battles"] = total_caught + random.randint(1, total_caught)
            data["gameStats"]["pokemonCaught"] = total_caught
            data["gameStats"]["pokemonSeen"] = total_seen
            data["gameStats"]["shinyPokemonCaught"] = len(data["dexData"]) * 2

            with open("data_Guest.json", "w") as f:
                json.dump(data, f, indent=2)


        
