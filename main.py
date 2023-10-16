import json
from character import Character


def read_characters_and_add_class(path):
    character_list = []
    with open (path) as archivo:
        datos = json.load(archivo)
    for i in datos:
        character_actual = Character(
            i["fields"]["name"],
            i["fields"]["created"],
            i["fields"]["gender"],
            i["fields"]["skin_color"], 
            i["fields"]["hair_color"], 
            i["fields"]["height"], 
            i["fields"]["eye_color"], 
            i["fields"]["mass"],
            i["fields"]["homeworld"],
            i["fields"]["birth_year"])   
        character_list.append(character_actual)
    
    return character_list
    
def main():
    character_list = read_characters_and_add_class("StarWars.json")
    character_list[0].__str__()

main()
