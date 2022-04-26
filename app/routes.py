from flask import Blueprint, jsonify, make_response, abort

class Planet:
    def __init__(self, id, name, description, order_in_solar_system):
        self.id = id
        self.name = name
        self.description = description
        self.order_in_solar_system = order_in_solar_system

    def to_json(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "description": self.description,
            "order in solar system": self.order_in_solar_system
        }

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
        planet_response.append(planet.to_json())
    return jsonify(planet_response), 200


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet
    return abort(make_response({"message":f"planet {planet_id} not found"}, 404))


@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet_id = validate_planet(planet_id)

    return jsonify(planet_id.to_json()), 200
    


