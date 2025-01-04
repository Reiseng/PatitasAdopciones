document.addEventListener('DOMContentLoaded', function () {
    // Mostrar/ocultar menú en pantallas pequeñas
    const menuToggle = document.querySelector('.menu-toggle span');
    const menu = document.querySelector('.menu');

    menuToggle.addEventListener('click', function () {
        menu.classList.toggle('open');
    });

    // Modo Oscuro
    const toggleDarkMode = document.getElementById('DarkMode');
    const modeIcon = document.getElementById('modeIcon');
    toggleDarkMode.style.cursor = 'pointer';

    // Verificar el modo guardado en localStorage y aplicar
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        modeIcon.classList.remove('fa-sun');
        modeIcon.classList.add('fa-moon');
    } else {
        document.body.classList.remove('dark-mode');
        modeIcon.classList.remove('fa-moon');
        modeIcon.classList.add('fa-sun');
    }

    toggleDarkMode.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
        
        // Cambiar el icono según el modo
        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'true');
            modeIcon.classList.remove('fa-sun');
            modeIcon.classList.add('fa-moon');
        } else {
            localStorage.setItem('darkMode', 'false');
            modeIcon.classList.remove('fa-moon');
            modeIcon.classList.add('fa-sun');
        }
    });
});