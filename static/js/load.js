async function loadEvents() {
    try {
        // Hacer la solicitud a la API para obtener los eventos
        const response = await fetch('/api/event');
        if (!response.ok) {
            throw new Error('Error al obtener los eventos');
        }
        const events = await response.json();
        
        // Obtener el contenedor donde se mostrarán los eventos
        const cardsContainer = document.getElementById('eventos-cards');

        // Limitar el número de eventos a 4
        const maxEvents = 4;
        const eventsToDisplay = events.slice(0, maxEvents);

        // Generar HTML dinámico para cada evento
        eventsToDisplay.forEach(event => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `
                <h4>${event.name}</h4> <!-- Accediendo al nombre del evento -->
                <p>Fecha: ${new Date(event.date).toLocaleDateString()}</p> <!-- Formateando la fecha -->
                <p>Descripción: ${event.description}</p> <!-- Accediendo a la descripción -->
                <a href="/event/detail?id=${event.id}">Ver más</a> <!-- Accediendo al ID del evento -->
            `;
            cardsContainer.appendChild(card);
        });
    } catch (error) {
        console.error(error);
    }
}

// Llamar a la función cuando la página esté lista
document.addEventListener('DOMContentLoaded', loadEvents);

