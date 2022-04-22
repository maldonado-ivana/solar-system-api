from flask import Blueprint, jsonify

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
planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods=["GET"])
def get_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id, 
            "name": planet.name, 
            "description": planet.description,
            "order in solar system": planet.order_in_solar_system
        })
    return jsonify(planet_response)
