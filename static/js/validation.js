document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    const userIdElement = document.getElementById('user-id');  // Obtener el ID del usuario
    if (!userIdElement) {
        console.log('No se encontró el campo con id_usuario');
    } else {
        console.log('ID Usuario:', userIdElement.value);
    }

    const form = document.getElementById('form');
    if (form) {
        console.log('Formulario encontrado');
        form.addEventListener('submit', async function (event) {
            event.preventDefault();  // Prevenir el envío por defecto del formulario
            console.log('Formulario enviado');
            const formData = new FormData(event.target);
            const data = {};
            formData.forEach((value, key) => {
                if (value.trim() !== '' && key !== '_method') {  // Excluir el campo _method
                    data[key] = value;
                }
            });

            const errorMessage = document.getElementById('error-message');
            const userId = userIdElement.value;  // Obtener el ID del usuario
            console.log('User ID:', userId);
            try {
                const response = await fetch('/api/user/' + userId, {  // Asignar la respuesta a `response`
                    method: 'PUT',  // Enviar como PUT
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),  // Enviar los datos como JSON
                });

                if (response.ok) {
                    window.location.href = '/panel'; // Redirige a la página deseada
                } else {
                    const errorData = await response.json();
                    errorMessage.textContent = errorData.message || 'Error desconocido';
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('Error en la solicitud:', error);
                errorMessage.textContent = 'Error en la solicitud: ' + error.message || 'Error desconocido';
                errorMessage.style.display = 'block';
            }
        });
    } else {
        console.log('Formulario no encontrado');
    }
});

    document.getElementById("form").addEventListener("input", function(event) {
        const currentPassword = document.getElementById("current_password").value;
        const newPassword = document.getElementById("new_password").value;
        const repeatPassword = document.getElementById("repeat_password").value;
        const errorMessage = document.getElementById("error-message");
        const errorPasswordMessage = document.getElementById("error-password-message");
        
        let isValid = true;

        // Verificar que la contraseña actual no esté vacía
        if (!currentPassword) {
                event.preventDefault();
                errorPasswordMessage.style.display = "block";
                errorPasswordMessage.textContent = "La contraseña actual es obligatoria.";
                isValid = false;
            } else {
                errorPasswordMessage.style.display = "none";
            }
            if (newPassword || repeatPassword){
            if (newPassword !== repeatPassword) {
                event.preventDefault();
                errorMessage.style.display = "block";
                isValid = false;
            } else {
                if (newPassword.length < 8){
                    event.preventDefault();
                    errorMessage.style.display = "block";
                    errorMessage.textContent = "La contraseña debe tener al menos 8 caracteres.";
                    isValid = false;
                    } else {
                        errorMessage.style.display = "none";
                        errorMessage.textContent = "Las contraraseñas no coinciden.";
                }
            }
        }

        // Si todo es válido, permite el envío
        if (isValid) {
            errorMessage.style.display = "none";
        }
    });

