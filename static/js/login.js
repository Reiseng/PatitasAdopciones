document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('form');
    const errorMessage = document.getElementById('error-message');

    if (loginForm) {
        loginForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const formData = new FormData(loginForm);
            const data = Object.fromEntries(formData.entries()); // Convierte formData en objeto

            try {
                const response = await fetch('/auth', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    const responseData = await response.json();
                    console.log('Login exitoso:', responseData.message);
                    window.location.href = '/panel'; // Redirige a la página deseada
                } else {
                    const errorData = await response.json();
                    errorMessage.textContent = errorData.message || 'Error desconocido';
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('Error en la solicitud:', error);
                errorMessage.textContent = 'Error inesperado. Por favor, inténtalo de nuevo.';
                errorMessage.style.display = 'block';
            }
        });
    }
});

const togglePassword = document.getElementById('togglePassword');
const passwordField = document.getElementById('password');
const passwordIcon = document.getElementById('passwordIcon');

togglePassword.addEventListener('click', () => {
    // Cambia el tipo del campo entre 'password' y 'text'
    const isPassword = passwordField.type === 'password';
    passwordField.type = isPassword ? 'text' : 'password';

    // Cambia la imagen
    passwordIcon.src = isPassword ? '/static/img/cerrar-ojo.png' : '/static/img/ojo.png';
});