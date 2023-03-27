function validData(){
    var user = document.getElementById("inputUser").value;
    var password = document.getElementById("inputPassword").value;
    var errorUsuario = document.getElementsByClassName("errorUsuario");
    if (user == ""){
        document.getElementById("errorUsuario").style.display = "block"; 
    }
}