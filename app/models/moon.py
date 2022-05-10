from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.String)
    description = db.Column(db.String)
    name = db.Column(db.String)
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="moons")

    # @classmethod
    # def create_moon(cls, request_body):
    #     new_moon = cls(
    #         name=request_body['name'],
    #         description=request_body['description'],
    #         size=request_body['size'],
    #         planet = planet
    #     )
    #     return new_moon
