from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, order_in_solar_system):
        self.id = id
        self.name = name
        self.description = description
        self.order_in_solar_system = order_in_solar_system

planets =  [
        Planet(1, "Mercury", "smallest", "first"),
        Planet(2, "Venus", "red, hot", "second"),
        Planet(3, "Earth", "our home", "third"),
        Planet(4, "Mars", "desert-like", "fourth"),
        Planet(5, "Jupiter", "largest", "fifth"),
        Planet(6, "Saturn", "lots o' rings", "sixth"),
        Planet(7, "Uranus", "smelly", "seventh"),
        Planet(8, "Neptune", "blue", "eigth")
]
