from app import db
from sqlalchemy import CheckConstraint

class Usuario(db.Model):
    __tablename__ = "TB_IMD_USUARIO"
    
    id = db.Column(db.Integer, primary_key=True)
    nm_usuario = db.Column(db.String(80), nullable = False)
    dt_nascimento = db.Column(db.Date, nullable = False)
    nr_cpf = db.Column(db.String(11), nullable = False, unique = True)
    
    id_tp_sanguineo = db.Column(
        db.Integer,
        db.ForeignKey("TB_IMD_TIPO_SANGUINEO.id_tp_sanguineo"),
        nullable = False
    )
    
    id_credencial = db.Column(
        db.Integer,
        db.ForeignKey("TB_IMD_CREDENCIAL.id_credencial"),
        nullable = False
    )
    
    id_plano_assinatura = db.Column(
        db.Integer,
        db.ForeignKey("TB_IMD_PLANO_ASSINATURA.id_plano"),
        nullable = False
    )
    
    __table_args__ = (
        CheckConstraint(
            "dt_nascimento <= GETDATE()",
            name="check_data_nascimento_valida"
        ),
    )