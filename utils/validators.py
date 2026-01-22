def validate_parte_form(form_data):
    errors = []
    
    # Validar campos obligatorios
    if not form_data.get('fecha_accidente'):
        errors.append('La fecha del accidente es obligatoria')
    
    if not form_data.get('lugar_accidente'):
        errors.append('El lugar del accidente es obligatorio')
    
    # Validar formato de email si se proporciona
    email_a = form_data.get('asegurado_a_contacto')
    if email_a and '@' not in email_a:
        errors.append('El email del asegurado A no es válido')
    
    return errors