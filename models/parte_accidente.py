from . import db
from datetime import datetime
import json

class ParteAccidente(db.Model):
    __tablename__ = 'partes_accidente'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Datos básicos del accidente
    fecha_accidente = db.Column(db.Date, nullable=False)
    hora_accidente = db.Column(db.String(10), nullable=False)  # Cambiado a String para mayor flexibilidad
    pais_accidente = db.Column(db.String(100), nullable=False, default='España')
    lugar_accidente = db.Column(db.String(200), nullable=False)
    victimas = db.Column(db.Boolean, default=False)
    
    # Datos Vehículo A
    asegurado_a_nombre = db.Column(db.String(100))
    asegurado_a_apellidos = db.Column(db.String(100))
    asegurado_a_direccion = db.Column(db.String(200))
    asegurado_a_codigo_postal = db.Column(db.String(10))
    asegurado_a_pais = db.Column(db.String(100))
    asegurado_a_contacto = db.Column(db.String(150))
    
    vehiculo_a_marca_modelo = db.Column(db.String(100))
    vehiculo_a_matricula = db.Column(db.String(20))
    vehiculo_a_pais_matricula = db.Column(db.String(50))
    
    aseguradora_a_nombre = db.Column(db.String(100))
    aseguradora_a_poliza = db.Column(db.String(50))
    aseguradora_a_carta_verde = db.Column(db.String(50))
    aseguradora_a_valida_desde = db.Column(db.Date)
    aseguradora_a_valida_hasta = db.Column(db.Date)
    aseguradora_a_agencia = db.Column(db.String(100))
    aseguradora_a_direccion = db.Column(db.String(200))
    aseguradora_a_contacto = db.Column(db.String(150))
    vehiculo_a_danos_asegurados = db.Column(db.Boolean, default=False)
    
    conductor_a_nombre = db.Column(db.String(100))
    conductor_a_apellidos = db.Column(db.String(100))
    conductor_a_fecha_nacimiento = db.Column(db.Date)
    conductor_a_direccion = db.Column(db.String(200))
    conductor_a_contacto = db.Column(db.String(150))
    conductor_a_permiso = db.Column(db.String(20))
    conductor_a_categoria = db.Column(db.String(10))
    conductor_a_permiso_valido_hasta = db.Column(db.Date)
    
    vehiculo_a_punto_choque = db.Column(db.String(100))
    vehiculo_a_danos = db.Column(db.Text)
    
    # Datos Vehículo B (similar al A)
    asegurado_b_nombre = db.Column(db.String(100))
    asegurado_b_apellidos = db.Column(db.String(100))
    asegurado_b_direccion = db.Column(db.String(200))
    asegurado_b_codigo_postal = db.Column(db.String(10))
    asegurado_b_pais = db.Column(db.String(100))
    asegurado_b_contacto = db.Column(db.String(150))
    
    vehiculo_b_marca_modelo = db.Column(db.String(100))
    vehiculo_b_matricula = db.Column(db.String(20))
    vehiculo_b_pais_matricula = db.Column(db.String(50))
    
    aseguradora_b_nombre = db.Column(db.String(100))
    aseguradora_b_poliza = db.Column(db.String(50))
    aseguradora_b_carta_verde = db.Column(db.String(50))
    aseguradora_b_valida_desde = db.Column(db.Date)
    aseguradora_b_valida_hasta = db.Column(db.Date)
    aseguradora_b_agencia = db.Column(db.String(100))
    aseguradora_b_direccion = db.Column(db.String(200))
    aseguradora_b_contacto = db.Column(db.String(150))
    vehiculo_b_danos_asegurados = db.Column(db.Boolean, default=False)
    
    conductor_b_nombre = db.Column(db.String(100))
    conductor_b_apellidos = db.Column(db.String(100))
    conductor_b_fecha_nacimiento = db.Column(db.Date)
    conductor_b_direccion = db.Column(db.String(200))
    conductor_b_contacto = db.Column(db.String(150))
    conductor_b_permiso = db.Column(db.String(20))
    conductor_b_categoria = db.Column(db.String(10))
    conductor_b_permiso_valido_hasta = db.Column(db.Date)
    
    vehiculo_b_punto_choque = db.Column(db.String(100))
    vehiculo_b_danos = db.Column(db.Text)
    
    # Circunstancias (almacenadas como JSON)
    circunstancias = db.Column(db.Text)  # JSON como string
    
    # Observaciones
    observaciones = db.Column(db.Text)
    
    # Firmas (como texto base64)
    firma_a = db.Column(db.Text)
    firma_b = db.Column(db.Text)
    
    def __repr__(self):
        return f'<ParteAccidente {self.id} - {self.fecha_accidente}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'fecha_accidente': self.fecha_accidente.isoformat() if self.fecha_accidente else None,
            'hora_accidente': self.hora_accidente,
            'lugar_accidente': self.lugar_accidente,
            'victimas': self.victimas,
            # ... agregar más campos según sea necesario
        }