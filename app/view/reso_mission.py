from flask_restful import Resource, reqparse
from app.Models.Mission import Mission
from flask import jsonify
from datetime import datetime

argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str )
argumentos.add_argument('release_date', type=str)
argumentos.add_argument('endpoint', type=str)
argumentos.add_argument('mission_state', type=str)
argumentos.add_argument('crew', type=str)
argumentos.add_argument('payload', type= str)
argumentos.add_argument('duration', type=str)
argumentos.add_argument('cost', type=str)
argumentos.add_argument('status', type= str)
#atualizar
argumentosatt = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentosatt.add_argument('id', type=int)
argumentosatt.add_argument('name', type=str)
argumentosatt.add_argument('release_date', type=str)
argumentosatt.add_argument('endpoint', type=str)
argumentosatt.add_argument('mission_state', type=str)
argumentosatt.add_argument('crew', type=str)
argumentosatt.add_argument('payload', type=str)
argumentosatt.add_argument('duration', type=str)
argumentosatt.add_argument('cost', type=str)
argumentosatt.add_argument('status', type= str)




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
            release_date = datetime.strptime(datas['release_date'], '%Y-%m-%d %H:%M:%S')
            duration = datetime.strptime(datas['duration'], '%Y-%m-%d %H:%M:%S')
            Mission.create_mission(self, datas['name'],release_date,datas['endpoint'],datas['mission_state'],datas['crew'],datas['payload'],duration,datas['cost'],datas['status'] )
            return {"message": 'Mission create succesfully'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
# class MissionRead(Resource):
#     def post(self):
#         try:
#             datas = argumentos.parse_args()
#             print(datas)
#             Mission.read_mission(self, datas['name'], datas['price'])
#             return {"message": 'Mission create succesfully'}, 200
#         except Exception as e:
#             return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionUpdate(Resource):
    def put(self):
        try:
            datas = argumentosatt.parse_args()
            release_date = datetime.strptime(datas['release_date'], '%Y-%m-%d %H:%M:%S')
            duration = datetime.strptime(datas['duration'], '%Y-%m-%d %H:%M:%S')
            print(datas)
            Mission.update_mission(self, datas['id'], datas['name'],release_date,datas['endpoint'],datas['mission_state'],datas['crew'],datas['payload'],duration,datas['cost'],datas['status'])
            return {"message": 'Mission update succesfully'}, 200
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