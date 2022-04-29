from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    order_in_ss = db.Column(db.String)

    def to_json(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "description": self.description,
            "order in solar system": self.order_in_ss
        }

        