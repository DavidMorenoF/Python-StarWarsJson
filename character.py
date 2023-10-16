class Character:
    name = None
    def __init__(self, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year):
        self._name = name
        self._created = created
        self._gender = gender
        self._skin_color = skin_color
        self._hair_color = hair_color
        self._height = height
        self._eye_color = eye_color
        self._mass = mass
        self._homeworld = homeworld
        self._birth_year = birth_year

    def __str__(self):
        print("El personatge " + self._name + " (" + self._gender + "), prové del món " + str(self._homeworld) + " i va nèixer l'any " + self._birth_year + ".")