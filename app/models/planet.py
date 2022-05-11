from app import db
from app.models.moon import Moon

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    order_in_ss = db.Column(db.String)
    moons = db.relationship("Moon", back_populates="planet")

    def to_json(self):
        names = []
        for moon in self.moons:
            names.append(moon.name)

        return {
            "id": self.id, 
            "name": self.name, 
            "description": self.description,
            "order in solar system": self.order_in_ss,
            "moons": names
        }

    def update_planet(self, update_body):
        self.name = update_body["name"]
        self.description = update_body["description"]
        self.order_in_ss = update_body["order in solar system"]

    @classmethod
    def create_planet(cls, request_body):
        new_planet = cls(
            name=request_body['name'],
            description=request_body['description'],
            order_in_ss=request_body['order in solar system']

        )
        return new_planet

        