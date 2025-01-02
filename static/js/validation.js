document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    const userId = document.getElementById('user-id')  // Obtener el ID del usuario
    if (!userId) {
        console.log('No se encontró el campo con id_usuario');
    } else {
        console.log('ID Usuario:', userId.value);
    }

    const form = document.getElementById('edit-user-form');
    if (form) {
        console.log('Formulario encontrado');
        form.addEventListener('submit', function (event) {
            event.preventDefault();  // Prevenir el envío por defecto del formulario
            console.log('Formulario enviado');
            const formData = new FormData(event.target);
            const data = {};
            formData.forEach((value, key) => {
                if (value.trim() !== '' && key !== '_method') {  // Excluir el campo _method
                    data[key] = value;
                }
            });

            const userId = document.getElementById('user-id').value;  // Obtener el ID del usuario
            console.log('User ID:', userId);

            fetch('/api/user/' + userId, {
                method: 'PUT',  // Enviar como PUT
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),  // Enviar los datos como JSON
            })
            .then(response => response.json())
            .then(data => console.log('Success:', data))
            .catch(error => console.error('Error:', error));
        });
    } else {
        console.log('Formulario no encontrado');
    }
});
