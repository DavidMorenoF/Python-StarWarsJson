import json
from character import Character
from character_films import Character_films


def read_characters_and_add_class(path):
    character_list = []
    with open (path) as archivo:
        characters = json.load(archivo)
    for character in characters:
        character_actual = Character(
            character["fields"]["name"],
            character["fields"]["created"],
            character["fields"]["gender"],
            character["fields"]["skin_color"], 
            character["fields"]["hair_color"], 
            character["fields"]["height"], 
            character["fields"]["eye_color"], 
            character["fields"]["mass"],
            character["fields"]["homeworld"],
            character["fields"]["birth_year"])   
        character_list.append(character_actual)
    
    return character_list

def pasar_a_character_films(lista):
    lista2 = []
    for character in lista:
        character_actual = Character_films(
            character.name,
            character.created,
            character.gender,
            character.skin_color, 
            character.hair_color, 
            character.height, 
            character.eye_color, 
            character.mass,
            character.homeworld,
            character.birth_year,
            )  
        match(character_actual.name):
            case "Luke Skywalker":
                character_actual.first_film = "Una Nueva Esperanza (1977)"
                character_actual.num_of_films = 6
                character_actual.alive_at_the_end = False
            case "Chewbacca":
                character_actual.first_film = "Una Nueva Esperanza (1977)"
                character_actual.num_of_films = 8
                character_actual.alive_at_the_end = True
            case "Anakin Skywalker":
                character_actual.first_film = "La Amenaza Fantasma (1999)"
                character_actual.num_of_films = 6
                character_actual.alive_at_the_end = False
            case _:
                character_actual.first_film = None
                character_actual.num_of_films = None
                character_actual.alive_at_the_end = None
            
        lista2.append(character_actual)
    return lista2
    
def parse_to_Json(list):
    pasar_a_json = []
    for i in list:
        pasar_a_json.append(i.__dict__)

    with open("StarWarsFilmsInfo.json", "w") as file:
        json.dump(pasar_a_json, file, indent=4)


def main():
    character_list = read_characters_and_add_class("StarWars.json")
    print(character_list[0].__str__())
    character_films_list= pasar_a_character_films(character_list)
    parse_to_Json(character_films_list)

main()
