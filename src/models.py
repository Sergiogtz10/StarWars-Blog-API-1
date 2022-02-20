from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
   
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    Birth = db.Column(db.String(120), nullable=False)
    Gender = db.Column(db.String(120), nullable=False)
    Heigth = db.Column(db.Integer)
    Skin_color = db.Column(db.String(120), nullable=False)
    Eyes_color = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth": self.Birth,
            "gender": self.Gender,
            "heigth": self.Heigth,
            "skin_color": self.Skin_color,
            "eyes_color": self.Eyes_color 
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    Climate = db.Column(db.Integer)
    Population = db.Column(db.Integer)
    Orbital_period = db.Column(db.Integer)
    Rotation_period = db.Column(db.Integer)
    Diameter = db.Column(db.Integer)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.Climate,
            "population": self.Population,
            "orbital_period": self.Orbital_period,
            "rotation_period": self.Rotation_period,
            "diameter": self.Diameter    
        }

class Userfavorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    Planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user = db.relationship(User)
    character = db.relationship(Characters)
    planets = db.relationship(Planets)

    def __repr__(self):
        return '< Userfavorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "User_id": self.User_id,
            "Characters_id": self.Characters_id,
            "Planets_id ": self.Planets_id ,
        }