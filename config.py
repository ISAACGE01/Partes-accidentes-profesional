import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la ruta base del proyecto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Clave secreta para sesiones y seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-clave-secreta-cambiar-en-produccion'
    
    # Configuración de base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'partes_accidente.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Otras configuraciones
    DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 't')