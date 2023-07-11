export function validData(){
  const emailFormat = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
  const userFormat = /^[a-zA-Z0-9]+$/;
    var valid = false;
    if(document.getElementById('username').value == ""){
    document.getElementById('errorUsuario').style.display = "inline";
    }
    if(document.getElementById('password').value == ""){
      document.getElementById('errorPassword').style.display = "inline";
    }
    if(document.getElementById('password').value != ""){
      document.getElementById('errorPassword').style.display = "none";
    }
    if(document.getElementById('username').value != ""){
      document.getElementById('errorUsuario').style.display = "none";
    }    
    if(document.getElementById('email').value == ""){
        document.getElementById('errorEmail').style.display = "inline";
    }
    if(document.getElementById('email').value != ""){
        document.getElementById('errorEmail').style.display = "none";
    }
    if((document.getElementById('password').value != "" & document.getElementById('username').value != "") & (emailFormat.test(document.getElementById('email').value) & userFormat.test(document.getElementById('username').value))){
      valid = true;
    }
    return valid;
  }