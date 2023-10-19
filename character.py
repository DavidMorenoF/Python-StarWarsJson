class Character:
    name = None
    def __init__(self, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year):
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year


    def __str__(self):
        return("El personatge " + self.name + " (" + self.gender + "), prové del món " + str(self.homeworld) + " i va nèixer l'any " + self.birth_year + ".")
    
