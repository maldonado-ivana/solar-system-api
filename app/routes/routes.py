from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
from .helpers import validate_planet
from app.models.moon import Moon

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def post_new_planet():
    request_body = request.get_json()
    
    new_planet = Planet.create_planet(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
    planets_response = [planet.to_json() for planet in planets]
        
    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_json()), 200


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    
    planet.update_planet(request_body)

    db.session.commit()

    return make_response(jsonify(f"Planet {planet.id} successfully updated"), 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet.id} successfully deleted"), 200)

@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    new_moon = Moon(
            name=request_body['name'],
            description=request_body['description'],
            size=request_body['size'],
            planet = planet
        )

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} part of \
        {new_moon.planet.name} successfully created"), 201)   

@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def read_all_moons(planet_id):
    planet = validate_planet(planet_id)

    moons_response = []
    for moon in planet.moons:
        moons_response.append(
            {
            "id": moon.id,
            "name": moon.name,
            "description": moon.description,
            "size": moon.size
            }
        )
    return jsonify(moons_response)