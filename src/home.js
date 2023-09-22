var id_access = localStorage.getItem("access_token");
var id_user = 0;

const getUser = await fetch('http://127.0.0.1:8000/id_user/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ id_access })
});
  
if (getUser.ok) {
  const data = await getUser.json();    
      id_user = data.Id;
} else {
  console.error('Error al obtener id de usuario');
}
var url = "http://127.0.0.1:8000/get_all_post/";
const getPost = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  });
  
if (getPost.ok) {
    var htmlContent = "";
    const data = await getPost.json();
    for (var i = 0; i < data.length ; i++){
      console.log(i);
      htmlContent  += `<p>Usuario: ${data[i][0]} <br>Estado: ${data[i][1]} <br>Fecha: ${data[i][2]}</p>`;
    }
     console.log(data);
     document.getElementById("news").innerHTML = htmlContent
} else {
    console.error('Error al recurerar publicaciones');
  }

async function publicarPost(){
  var contenido = document.getElementById("text");
  const postUp = await fetch('http://127.0.0.1:8000/addpost/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ id_user, contenido })
  });
    
  if (postUp.ok) {
    console.log('ok');
  } else {
    console.error('Error al obtener id de usuario');
  } 
}
