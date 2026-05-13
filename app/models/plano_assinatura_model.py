from app import db

class PlanoAssinatura(db.Model):
    __tablename__ = "TB_IMD_PLANO_ASSINATURA"
    
    id_plano = db.Column(db.Integer, primary_key = True)
    nm_plano = db.Column(db.String(10), nullable = False)
    vl_plano = db.Column(db.Numeric(4,2), nullable = False)
    ds_beneficios = db.Column(db.String(255), nullable = False)