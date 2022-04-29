from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def post_new_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    order_in_ss = request_body["order in solar system"] )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)



planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_json())
        
    return jsonify(planets_response)


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     return abort(make_response({"message":f"planet {planet_id} not found"}, 404))


# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_one_planet(planet_id):
#     planet_id = validate_planet(planet_id)

#     return jsonify(planet_id.to_json()), 200
    


