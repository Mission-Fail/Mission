from app import db

class Mission(db.Model):
    __tablename__ = 'mission'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    endpoint = db.Column(db.String)
    mission_state = db.Column(db.String)
    crew = db.Column(db.String)
    payload = db.Column(db.String)
    duration = db.Column(db.DateTime)
    cost = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, name,release_date,endpoint,mission_state,crew,payload,duration,cost,status):
        self.name = name
        self.release_date = release_date
        self.endpoint = endpoint
        self.mission_state = mission_state
        self.crew = crew
        self.payload = payload
        self.duration = duration
        self.cost = cost
        self.status = status 
     
    def create_mission(self,name,release_date,endpoint,mission_state,crew,payload,duration,cost,status):
        try:
            add_banco = Mission(name,release_date,endpoint,mission_state,crew,payload,duration,cost,status)
            print(add_banco)
            db.session.add(add_banco) 
            db.session.commit()
        except Exception as error:
            print("Não foi possível criar a missão!", error)

    def update_mission(self, id, name, release_date, endpoint, mission_state, crew, payload, duration, cost, status ):
        try:
            db.session.query(Mission).filter(Mission.id==id).update({"name":name,"release_date":release_date,"endpoint":endpoint, "mission_state":mission_state, "crew":crew, "payload":payload, "duration":duration, "cost":cost ,"status":status })
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as error:
            print("Falha ao dar upadate na missão", error)

    def delete_mission(self, id):
        try:
            db.session.query(Mission).filter(Mission.id==id).delete()
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as error:
            print("Falha ao deletar a missão", error)

