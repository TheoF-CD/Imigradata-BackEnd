from app import db

class Credencial(db.Model):
    __tablename__ = "TB_IMD_CREDENCIAL"
    
    id_credencial = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, nullable = False)
    senha = db.Column(db.String(255), unique = True, nullable = False)
    dt_criacao = db.Column(db.Date, nullable = False)