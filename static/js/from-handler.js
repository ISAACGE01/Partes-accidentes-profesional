function guardarParte() {
    const formData = new FormData(document.getElementById('parte-form'));
    
    // Agregar firmas como datos base64
    formData.append('firmaA', getSignatureData('signatureA'));
    formData.append('firmaB', getSignatureData('signatureB'));
    
    fetch('/partes/guardar', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Parte guardado correctamente');
            // Redirigir o mostrar mensaje de éxito
            window.location.href = '/partes/exito/' + data.parte_id;
        } else {
            alert('Error al guardar el parte: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error de conexión');
    });
}

function initFormValidation() {
    const form = document.getElementById('parte-form');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Validaciones básicas
        const fecha = document.getElementById('fecha-accidente').value;
        const lugar = document.getElementById('lugar-accidente').value;
        
        if (!fecha || !lugar) {
            alert('Por favor, complete los campos obligatorios');
            return false;
        }
        
        return true;
    });
}