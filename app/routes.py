from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)    
    if not planet: 
        return abort(make_response({"message":f"planet {planet_id} not found"}, 404))
        
    return planet 


@planets_bp.route("", methods=["POST"])
def post_new_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    order_in_ss = request_body["order in solar system"] )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = [planet.to_json() for planet in planets]
        
    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json()), 200


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    update_body = request.get_json()
    planet = validate_planet(planet_id)

    planet.name = update_body["name"]
    planet.description = update_body["description"]
    planet.order_in_ss = update_body["order in solar system"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted", 200)


# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_one_planet(planet_id):
#     planet_id = validate_planet(planet_id)

#     return jsonify(planet_id.to_json()), 200
    


