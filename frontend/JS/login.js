const userp = document.getElementById("username");
const passwordp = document.getElementById("password");
const tokenp = document.getElementById("tokenp"); // Elemento donde mostrarás el token
const facebook = document.getElementById("Facebook");

facebook.href = "https://www.facebook.com"

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
    });
}
