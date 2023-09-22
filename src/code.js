const form = document.getElementById('formulario');
var id_access = localStorage.getItem("access_token");
if(id_access){
fetch("http://127.0.0.1:8000/valid_token/", {
  method: 'POST', // Utiliza el método POST
  headers: {
    'Authorization': `Bearer ${id_access}`,
    'Content-Type': 'application/json',
  },
})
  .then(response => {
    if (!response.ok) {
      throw new Error('Error en la solicitud');
    }
    return response.json();
  })
  .then(data => {
    // Maneja la respuesta del backend aquí
    console.log(data);
      window.location.href = "/home.html";
  })
  .catch(error => {
    console.error('Error:', error);
  });	
}

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
      window.location.href = "/home.html";
    } else {
    console.error('Error al iniciar sesión');
  }
  } catch (error) {
    console.error('Error:', error);
  }
  });
