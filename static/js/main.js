const facebook = document.getElementById("Facebook");

facebook.href = "https://www.facebook.com"

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