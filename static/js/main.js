document.addEventListener('DOMContentLoaded', function() {
    // Inicializar funcionalidades
    initSignatures();
    initFormValidation();
    setupEventListeners();
});

function setupEventListeners() {
    // Contador de casillas marcadas
    const checkboxes = document.querySelectorAll('.circumstances-grid input[type="checkbox"]');
    const counter = document.getElementById('casillas-marcadas');
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const checked = document.querySelectorAll('.circumstances-grid input[type="checkbox"]:checked');
            counter.value = checked.length;
        });
    });
    
    // Botón de guardar
    document.getElementById('btn-guardar').addEventListener('click', guardarParte);
    
    // Botón de imprimir
    document.getElementById('btn-imprimir').addEventListener('click', function() {
        window.print();
    });
}