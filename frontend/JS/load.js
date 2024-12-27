function getUsers(){
    const getUrl = 'http://127.0.0.1:5000/user/'
    const token = localStorage.getItem('authToken');
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
        const getusersp = document.getElementById("getusers");
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
};