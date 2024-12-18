document.addEventListener('DOMContentLoaded', function () {
    // Botón que confirma la eliminación en el modal
    const confirmDeleteModalBtn = document.getElementById('confirm-delete-modal-btn');
    // Formulario oculto para eliminar la tarea
    const deleteForm = document.getElementById('delete-form');
    
    console.log('DOM content loaded');

    // Validamos que ambos elementos existan
    if (confirmDeleteModalBtn && deleteForm) {
        console.log('Elementos encontrados');
        // Vinculamos el evento al botón de confirmación
        confirmDeleteModalBtn.addEventListener('click', function () {
            console.log('Botón de confirmación presionado');
            // Enviar formulario al confirmar
            deleteForm.submit();
        });
    } else {
        console.error('No se encontró el botón de confirmación o el formulario en el DOM.');
    }

    // Agregar un listener para el evento 'show.bs.modal'
    const deleteModal = document.getElementById('deleteModal');
    if (deleteModal) {
        deleteModal.addEventListener('show.bs.modal', function () {
            console.log('Modal se está mostrando');
        });
    }
});
