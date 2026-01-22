from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from models import db
from models.parte_accidente import ParteAccidente
from datetime import datetime
import json

partes_bp = Blueprint('partes', __name__)

@partes_bp.route('/nuevo')
def nuevo_parte():
    return render_template('parte_form.html')

@partes_bp.route('/guardar', methods=['POST'])
def guardar_parte():
    try:
        print("Recibiendo datos del formulario...")
        
        # Crear nuevo parte
        nuevo_parte = ParteAccidente(
            # Datos básicos
            fecha_accidente=datetime.strptime(request.form.get('fecha_accidente'), '%Y-%m-%d').date() if request.form.get('fecha_accidente') else None,
            hora_accidente=request.form.get('hora_accidente', ''),
            pais_accidente=request.form.get('pais_accidente', 'España'),
            lugar_accidente=request.form.get('lugar_accidente', ''),
            victimas=bool(request.form.get('victimas')),
            
            # Vehículo A
            asegurado_a_nombre=request.form.get('asegurado_a_nombre', ''),
            asegurado_a_apellidos=request.form.get('asegurado_a_apellidos', ''),
            asegurado_a_direccion=request.form.get('asegurado_a_direccion', ''),
            asegurado_a_codigo_postal=request.form.get('asegurado_a_codigo_postal', ''),
            asegurado_a_pais=request.form.get('asegurado_a_pais', 'España'),
            asegurado_a_contacto=request.form.get('asegurado_a_contacto', ''),
            
            vehiculo_a_marca_modelo=request.form.get('vehiculo_a_marca_modelo', ''),
            vehiculo_a_matricula=request.form.get('vehiculo_a_matricula', ''),
            vehiculo_a_pais_matricula=request.form.get('vehiculo_a_pais_matricula', 'España'),
            
            # ... agregar más campos según sea necesario
            observaciones=request.form.get('observaciones', '')
        )
        
        db.session.add(nuevo_parte)
        db.session.commit()
        
        print(f"Parte guardado con ID: {nuevo_parte.id}")
        
        return jsonify({
            'success': True, 
            'parte_id': nuevo_parte.id,
            'message': 'Parte guardado correctamente'
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error al guardar: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@partes_bp.route('/exito/<int:parte_id>')
def exito(parte_id):
    return render_template('success.html', parte_id=parte_id)

@partes_bp.route('/lista')
def lista_partes():
    partes = ParteAccidente.query.order_by(ParteAccidente.fecha_creacion.desc()).all()
    return render_template('lista_partes.html', partes=partes)