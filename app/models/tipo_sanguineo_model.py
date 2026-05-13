from app import db 

class TipoSanguineo(db.Model):
    __tablename__ = "TB_IMD_TIPO_SANGUINEO"
    
    id_tp_sanguineo = db.Column(db.Integer, primary_key = True)
    nm_tipo_sanguineo = db.Column(db.String(3), unique = True, nullable = False)