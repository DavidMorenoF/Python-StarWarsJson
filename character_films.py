from character import Character


class Character_films(Character):
    

    def __init__(self, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year, num_of_films, first_film, alive_at_the_end):
        super().__init__(name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self.__num_of_films = num_of_films

    
    @num_of_films.setter
    def num_of_films(self, num):
        self.__num_of_films = num
        