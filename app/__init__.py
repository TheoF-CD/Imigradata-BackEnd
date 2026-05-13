from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.usuario_model import Usuario
    from app.models.tipo_sanguineo_model import TipoSanguineo
    from app.models.plano_assinatura_model import PlanoAssinatura
    from app.models.credencial_model import Credencial

    return app