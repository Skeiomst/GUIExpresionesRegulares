// Función para validar un campo en tiempo real
async function validateField(field) {
    const fieldName = field.name;
    const value = field.value;

    const response = await fetch('/validate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ field_name: fieldName, value: value })
    });

    const result = await response.json();
    const checkbox = document.getElementById(fieldName + '_checkbox');

    if (result.valid) {
        checkbox.checked = true;
    } else {
        checkbox.checked = false;
    }

    updateSubmitButtonState();
}

// Función para verificar si todos los checkboxes están marcados
function updateSubmitButtonState() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const submitButton = document.getElementById('submitButton');
    const allValid = Array.from(checkboxes).every(checkbox => checkbox.checked);

    submitButton.disabled = !allValid;
}

// Función para mostrar la alerta
function showSuccessAlert(event) {
    event.preventDefault();
    Swal.fire({
        title: '¡Éxito!',
        text: 'Todos los campos están validados correctamente.',
        icon: 'success',
        confirmButtonText: 'Aceptar'
    });
}
