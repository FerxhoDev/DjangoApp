document.addEventListener('DOMContentLoaded', function () {
    const deleteButton = document.getElementById('delete-button');
    const deleteForm = document.getElementById('delete-form');

    deleteButton.addEventListener('click', function () {
        const confirmDelete = confirm('¿Estás seguro de que deseas eliminar esta tarea?');
        if (confirmDelete) {
            deleteForm.submit();
        }
    });
});
