import { validUser } from './user.js';

const form1 = document.querySelector('#formulario');

form1.addEventListener('submit', async (event) => {
  event.preventDefault();
  const username = document.getElementById('inputUser').value;
  const password = document.getElementById('inputPassword').value;
  if (validUser() == true ){

    
    const response = await fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });
    
    if (response.ok) {
      	var data = await response.text();
      	var dataObj = JSON.parse(data);
	var sessionId = dataObj.session_id;
	sessionStorage.setItem("session_id", sessionId);
	console.log(sessionId);
    } else {
      console.error('Error al iniciar sesión');
    }
  }
});
