document.getElementById("root").innerHTML = `
    <div id="top-var"></div>
    <div id="postNews">
        <input type="text">
        <button id="postNew" type="submit">Publicar Post</button>
    </div>
    <div id="news-div">
            <p> Últimas publicaciones </p>
            <div id="news">
                //Últimas 20 publicaciones
            </divs>
    </div>
`;

const response = await fetch('http://127.0.0.1:8000/lastpost/3', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  });
  
  if (response.ok) {
    const data = await response.json();    
        document.getElementById("news").innerHTML = `<p>  ${data} </p>`
} else {
    console.error('Error recurerar publicaciones');
  }

/*
await fetch("http://127.0.0.1:8000/user/nicovega/")
    .then(res => res.json())
    .then(response => {
        document.getElementById("news").innerHTML = ` <p>${response.Nombre} </p> <p>${response.fecha_registro} </p>`;
    })
*/
//document.getElementById("root").innerHTML = "<p>Hola mundo</p>";