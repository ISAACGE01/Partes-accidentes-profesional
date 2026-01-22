from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar modelos después de inicializar db para evitar importaciones circulares
from .parte_accidente import ParteAccidente