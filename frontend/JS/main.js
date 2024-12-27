function getUsers(){
    const getUrl = 'http://127.0.0.1:5000/user/'
    const token = localStorage.getItem('authToken');
    fetch(getUrl,{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token  // Incluye el token en el encabezado
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const getusersp = document.getElementById("getusers");
        getusersp.textContent = 'ID: ' + data[0][0] + " Mail: " + data[0][1] + " Nombre: " + data[0][2] + " Rango: " + data[0][3];
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
};

function getCompany(){
    const getUrl = 'http://127.0.0.1:5000/company/'
    fetch(getUrl,{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const company = data[0];
         companyName = company.nombre;
         companyMail = company.mail;
         companyTel = company.telefono;
         companyFacebook = company.facebook;
         companyInstagram = company.instagram;
         companyTwitter = company.twitter;

    })
    .catch(error => {
        console.error('Error:', error);
    });
};