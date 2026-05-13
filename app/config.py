import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://sa:1um2doiS%40@THEO/ImigraData?"
        "driver=ODBC+Driver+17+for+SQL+Server"
        "&TrustServerCertificate=yes"
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False