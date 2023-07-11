import { validUser } from './user.js';


const form = document.getElementById('formulario');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  const formData = new URLSearchParams();
  formData.append('username', username);
  formData.append('password', password);

  try {
    const response = await fetch('http://127.0.0.1:8000/login/', {
      method: 'POST',
      body: formData,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });

    if (response.ok) {
      var data = await response.text();
      var dataObj = JSON.parse(data);
      var access_token = dataObj.access_token;
      localStorage.setItem("access_token", access_token);
      console.log(access_token);
    } else {
    console.error('Error al iniciar sesión');
  }
  } catch (error) {
    console.error('Error:', error);
  }
});