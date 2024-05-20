from flask_restful import Resource, reqparse
from app.models.mission import Mission
from flask import jsonify

argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=int)
argumentos.add_argument('release_date', type=int )
argumentos.add_argument('destiny', type=int)
argumentos.add_argument('mission state', type=int)
argumentos.add_argument('crew', type=int)
argumentos.add_argument('useful load', type=int)
argumentos.add_argument('mission_duration', type=int)
argumentos.add_argument('cost', type= int)
argumentos.add_argument('status', type= int)
#atualizar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('id', type=str)
argumentos.add_argument('name', type=str)
argumentos.add_argument('release_date', type=str)
argumentos.add_argument('destiny', type=str)
argumentos.add_argument('mission state', type=str)
argumentos.add_argument('crew', type=str)
argumentos.add_argument('useful load', type=str)
argumentos.add_argument('mission duration', type=str)
argumentos.add_argument('cost', type=str)
argumentos.add_argument('status', type= str)




#deletar
argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Welcome to my aplication flask")

class MissionCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            Mission.save_mission(self, datas['name'], datas['price'])
            return {"message": 'Mission create succesfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class MissionRead(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            Mission.read_mission(self, datas['name'], datas['price'])
            return {"message": 'Mission create succesfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionUpdate(Resource):
    def put(self):
        try:
            #datas = argumentos_update.parse_args()#////////
           ##print(datas)##
           ## Mission.update_mission(self, datas['id'], datas['name'], datas['price'])##
            return {"message": 'Products update succesfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            print(datas)
            Mission.delete_mission(self, datas['id'])
            return {"message": ' deleted'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500