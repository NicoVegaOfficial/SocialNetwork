const form1 = document.querySelector('#formulario');

form1.addEventListener('submit', async (event) => {
  event.preventDefault();
  const username = document.getElementById('inputUser').value;
  const password = document.getElementById('inputPassword').value;
  if (validData() == true ){

    
    const response = await fetch('http://127.0.0.1:8000/login/', {
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

function validData(){
  var format = /^[a-zA-Z0-9]+$/;
  var valid = false;
  if(document.getElementById('inputUser').value == ""){
  document.getElementById('errorUsuario').style.display = "inline";
  }
  if(document.getElementById('inputPassword').value == ""){
    document.getElementById('errorPassword').style.display = "inline";
  }
  if(document.getElementById('inputPassword').value != ""){
    document.getElementById('errorPassword').style.display = "none";
  }
  if(document.getElementById('inputUser').value != ""){
    document.getElementById('errorUsuario').style.display = "none";
  }
  if((document.getElementById('inputPassword').value != "" & document.getElementById('inputUser').value != "") & (format.test(document.getElementById('inputUser').value))){
    valid = true;
  }
  return valid;
}