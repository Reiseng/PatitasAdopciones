    // Función para cargar los eventos desde la API
    async function loadEvents() {
        try {
            // Hacer la solicitud a la API para obtener los eventos
            const response = await fetch('/events/');
            if (!response.ok) {
                throw new Error('Error al obtener los eventos');
            }
            const events = await response.json();
            // Obtener el contenedor donde se mostrarán los eventos
            const cardsContainer = document.getElementById('eventos-cards');

            // Generar HTML dinámico para cada evento
            events.forEach(event => {
                const card = document.createElement('div');
                card.classList.add('card');
                card.innerHTML = `
                    <h4>${event[1]}</h4> <!-- Accediendo al nombre del evento -->
                    <p>Fecha: ${new Date(event[2]).toLocaleDateString()}</p> <!-- Formateando la fecha -->
                    <p>Descripción: ${event[3]}</p> <!-- Accediendo a la descripción -->
                    <a href="/event?id=${event[0]}">Ver más</a> <!-- Accediendo al ID del evento -->
                `;
                cardsContainer.appendChild(card);
            });
        } catch (error) {
            console.error(error);
        }
    }
    
    // Llamar a la función cuando la página esté lista
    document.addEventListener('DOMContentLoaded', loadEvents);