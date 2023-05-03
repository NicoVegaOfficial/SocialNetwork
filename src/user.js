export function validUser(){
    const format = /^[a-zA-Z0-9]+$/;
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
    if(document.getElementById('inputEmail').value == ""){
        document.getElementById('errorEmail').style.display = "inline";
    }
    if(document.getElementById('inputEmail').value != ""){
        document.getElementById('errorEmail').style.display = "none";
    }
    if((document.getElementById('inputPassword').value != "" & document.getElementById('inputUser').value != "") & (format.test(document.getElementById('inputUser').value))){
      valid = true;
    }
    return valid;
  }