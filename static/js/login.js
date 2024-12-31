const userp = document.getElementById("username");
const passwordp = document.getElementById("password");
const tokenp = document.getElementById("tokenp"); // Elemento donde mostrarás el token


function login(event) {
    // Evita el comportamiento predeterminado del formulario
    event.preventDefault();

    const loginUrl = 'http://127.0.0.1:5000/auth/';

    // Obtén los valores de los inputs
    const credentials = {
        mail: userp.value,
        password: passwordp.value
    };

    fetch(loginUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Guarda el token en localStorage
        localStorage.setItem('authToken', data.token);
    })
    .catch(error => {
    })
};
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