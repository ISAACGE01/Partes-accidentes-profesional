from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

def generate_pdf(parte):
    filename = f"parte_{parte.id}.pdf"
    filepath = os.path.join('data', 'partes', filename)
    
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    # Configurar el PDF
    c.setFont("Helvetica", 10)
    
    # Agregar contenido del parte al PDF
    c.drawString(50, height - 50, "DECLARACIÓN AMISTOSA DE ACCIDENTE")
    c.drawString(50, height - 70, f"Fecha del accidente: {parte.fecha_accidente}")
    # ... continuar con todo el contenido
    
    c.save()
    return filepath