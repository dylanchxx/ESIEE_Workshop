# DEFINE CLASS
class Superhero:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

# Création d'un objet
IronMan = Superhero("IronMan")
IronMan.printname()

# ADD POWERS AND FRIENDS ATTRIBUTES
class Superhero:
    def __init__(self, name, powers, friends):
        self.name = name
        self.powers = powers
        self.friends = friends

    def printname(self):
        print(self.name)

    def printpowers(self):
        print(self.powers)

    def printfriends(self):
        print(self.friends)

    def printAttributes(self):
        print(f"Name: {self.name}, Powers: {self.powers}, Friends: {self.friends}")

# Création d'objets avec les bons types
Ironman = Superhero("IronMan", ["SuperStrength", "Flight"], ["SpiderMan", "Thor"])
Ironman.printAttributes()

SpiderMan = Superhero("SpiderMan", ["Invisibility", "Wall-Crawling"], ["IronMan", "Thor"])
SpiderMan.printAttributes()

# ADD METHODS TO USE 5 Superpowers. Method must initialize a power

class Superhero:
    def __init__(self, name, powers, friends):
        self.name = name
        self.powers = powers
        self.friends = friends

    def printname(self):
        print(self.name)

    def printpowers(self):
        print(self.powers)

    def printfriends(self):
        print(self.friends)

    def printAttributes(self):
        print(f"Name: {self.name}, Powers: {self.powers}, Friends: {self.friends}")

    def usePower(self, power):
        if power in self.powers:
            print(f"{self.name} is using {power}!")
        else:
            print(f"{self.name} does not have the power: {power}.")

#Create Actions and use superpowers
CaptainMarvel = Superhero(
    name="Captain Marvel",
    powers=["Energy Blast", "Flight", "SuperStrength", "Durability", "Cosmic Awareness"],
    friends=["Nick Fury", "IronMan"]
)

CaptainMarvel.printAttributes()

CaptainMarvel.usePower("Flight")
CaptainMarvel.usePower("Invisibility")  # Pouvoir non possédé

