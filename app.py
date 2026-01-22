from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializar extensions primero
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(Config)
    
    # Verificar que la configuración se cargó correctamente
    print("DATABASE URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))
    print("SECRET KEY:", app.config.get('SECRET_KEY'))
    
    # Inicializar extensiones con la app
    db.init_app(app)
    
    # Registrar blueprints
    from routes.partes import partes_bp
    app.register_blueprint(partes_bp, url_prefix='/partes')
    
    # Crear tablas en la base de datos
    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente")
    
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)