from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'

db = SQLAlchemy(app)
from app.Models.Mission import Mission
with app.app_context():
    db.create_all()

from app.view.reso_mission import Index
from app.view.reso_mission import MissionId
from app.view.reso_mission import MissionCreate
from app.view.reso_mission import MissionUpdate
from app.view.reso_mission import MissionDelete

api.add_resource(Index, '/')
api.add_resource(MissionId, '/buscar')
api.add_resource(MissionCreate, '/criar') # post
api.add_resource(MissionUpdate, '/atualizar') # put
api.add_resource(MissionDelete, '/deletar') # delete

''' @app.route("/")
def index():
    # return "<h1> Minha aplicacao em flask </h1>"
    return render_template("index.html") '''