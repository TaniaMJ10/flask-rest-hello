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
from models import db, User, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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
    
    users = User.query.all()
    if len(users) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_users = list(map(lambda x: x.serialize(), users))
    return serialized_users, 200

@app.route('/characters', methods=['GET'])
def handle_characters():
    
    characters = Characters.query.all()
    if len(characters) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_characters = list(map(lambda x: x.serialize(), characters))
    return serialized_characters, 200

@app.route('/planets', methods=['GET'])
def handle_planets():
    
    planets = Planets.query.all()
    if len(planets) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_planets = list(map(lambda x: x.serialize(), planets))
    return serialized_planets, 200

@app.route('/favorites', methods=['GET'])
def handle_favorites():
    
    favorites = Favorites.query.all()
    if len(favorites) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_favorites = list(map(lambda x: x.serialize(), favorites))
    return serialized_favorites, 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": f"user with id {user_id} not found"}), 404
    serialized_user = user.serialize()
    return serialized_user, 200

@app.route('/characters/<int:characters_id>', methods=['GET'])
def get_one_chartacters(characters_id):
    characters = Characters.query.get(characters_id)
    if characters is None:
        return jsonify({"msg": f"characters with id {characters_id} not found"}), 404
    serialized_characters = characters.serialize()
    return serialized_characters, 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_one_planets(planets_id):
    planets = Planets.query.get(planets_id)
    if planets is None:
        return jsonify({"msg": f"user with id {planets_id} not found"}), 404
    serialized_planets = planets.serialize()
    return serialized_planets, 200

@app.route('/favorites/<int:favorites_id>', methods=['GET'])
def get_one_favorites(favorites_id):
    favorites = Favorites.query.get(favorites_id)
    if favorites is None:
        return jsonify({"msg": f"user with id {favorites_id} not found"}), 404
    serialized_favorites = favorites.serialize()
    return serialized_favorites, 200











# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
