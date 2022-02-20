"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Userfavorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



#[GET] /people Get a list of all the people in the database

@app.route('/People', methods=['GET'])
def get_AllPeople():
    People_list = []
    people = Characters.query.all()
    for characters in people:
        People_list.append(characters.serialize())
    return jsonify(People_list), 200

# [GET] /people/<int:people_id> Get a one single people information

@app.route('/People/<id>',  methods=['GET'])
def get_People(id):
    peoples = Characters.query.get(id)
    return jsonify(peoples.serialize()), 200

#[GET] /planets Get a list of all the planets in the database

@app.route('/Planets', methods=['GET'])
def get_AllPlanets():
    Planets_list = []
    planets = Planets.query.all()
    for planet in planets:
        Planets_list.append(planet.serialize())
    return jsonify(Planets_list), 200

#[GET] /planets/<int:planet_id>

@app.route('/Planets/<id>',  methods=['GET'])
def get_Planets(id):
    planets = Planets.query.get(id)
    return jsonify(planets.serialize()), 200

#[GET] /users Get a list of all the blog post users

@app.route('/users', methods=['GET'])
def get_AllUser():
    User_list = []
    users = User.query.all()
    for user in users:
        User_list.append(user.serialize())
    return jsonify(User_list), 200

#[GET] /users/favorites Get all the favorites that belong to the current user.

@app.route('/users/favorites', methods=['GET'])
def get_UserFavorites():
    Userfavorites_list = []
    favorites = Userfavorite.query.all()
    for user in favorites:
        Userfavorites_list.append(user.serialize())
    return jsonify(Userfavorites_list), 200

#[POST] /favorite/planet/<int:planet_id> Add a new favorite planet to the current user with the planet id = planet_id.

@app.route('/favorite/planet/<id>', methods=['POST'])
def post_Planetfavorites():
    body = request.get_json()
    planetsfavorites_post = Planets(Planets_id=body['Planets_id'], User_id=body['User_id'])
    db.session.add(planetsfavorites_post)
    db.session.commit()
    return jsonify(planetsfavorites_post.serialize()), 200

#[POST] /favorite/people/<int:planet_id> Add a new favorite people to the current user with the people id = people_id.

@app.route('/favorite/people/<id>', methods=['POST'])
def post_Peoplefavorites():
    body = request.get_json()
    peoplefavorites_post = Characters(Characters_id=body['Characters_id'], User_id=body['User_id'])
    db.session.add(peoplefavorites_post)
    db.session.commit()
    return jsonify(peoplefavorites_post.serialize()), 200

#[DELETE] /favorite/planet/<int:planet_id> Delete favorite planet with the id = planet_id.

@app.route('/favorite/planet/<Planets_id>', methods=['DELETE'])
def post_Planetfavorites(Planets_id):
    planetsfavorites_delete = UserFavorite.query.get(Planets_id)
    db.session.delete(planetsfavorites_delete)
    db.session.commit()
    return jsonify(planetsfavorites_delete.serialize()), 200

#[DELETE] /favorite/people/<int:people_id> Delete favorite people with the id = people_id.

@app.route('/favorite/peoples/<Characters_id>', methods=['DELETE'])
def delete_Peoplefavorites(Characters_id):
    peoplefavorites_delete = UserFavorite.query.get(Characters_id)
    db.session.delete(peoplefavorites_delete)
    db.session.commit()
    return jsonify(peoplefavorites_delete.serialize()), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
