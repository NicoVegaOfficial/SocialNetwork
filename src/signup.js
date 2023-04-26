import { validData } from './data.js';

const form1 = document.querySelector('#formulario');
form1.addEventListener('submit', async (event) => {
  event.preventDefault();
  const username = document.getElementById('inputUser').value;
  const password = document.getElementById('inputPassword').value;
  if (validData() == true ){

    
    const response = await fetch('http://127.0.0.1:8000/adduser/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });
    
    if (response.ok) {
      const data = await response.json();
      console.log(data);
    } else {
      console.error('Error al iniciar sesión');
    }
  }
});