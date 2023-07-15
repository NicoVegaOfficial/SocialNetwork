async function publicarPost(){
    var id_access = localStorage.getItem("access_token");
    var contenido = document.getElementById("text").value;
    const postUp = await fetch('http://127.0.0.1:8000/addpost/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ id_access, contenido }),
      
    });
    console.log(JSON.stringify({ id_access, contenido }))
    if (postUp.ok) {
      console.log('ok');
    } else {
      console.error('Error al obtener id de usuario');
    } 
  }