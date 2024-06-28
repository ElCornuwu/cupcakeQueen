function validarLog() {
    document.getElementById("Login").addEventListener("submit", function(event){event.preventDefault();});
    var logMail = document.getElementById("LoginEmail").value;
    var mailLogError = document.getElementById('valCorreoLog');
    var logPass = document.getElementById('LoginPass').value;
    var PassLogError =document.getElementById('valPassLog');


    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(logMail)) { 
        mailLogError.innerText = 'Formato de correo no válido.';

    } else {
        mailLogError.innerText = '';
    }
    if (logPass.length < 8) {
        PassLogError.innerText = 'Ingrese contraseña.';
    }else{
        PassLogError.innerText = '';
    }

    if(mailLogError.innerText === '' && PassLogError.innerText === ''){
        alert('Se inicio sesión correctamente.');
    }
    return false;
}

function validarReg(){
    document.getElementById("Reg").addEventListener("submit", function(event){event.preventDefault();});
    var nombre = document.getElementById('RegInputName').value;
    var valNom = document.getElementById('valNombReg');
    var apell = document.getElementById('RegInputLastName').value;
    var valApell = document.getElementById('valApellReg');
    var mail = document.getElementById('RegInputEmail').value;
    var valMail = document.getElementById('valCorreoReg');
    var pass = document.getElementById('RegInputPassword').value;
    var valPass = document.getElementById('valPassReg');
    var pass1 = document.getElementById('RegInputPassword1').value;
    var valPass1 = document.getElementById('valPassReg1');
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (nombre.length < 3) {
        valNom.innerText = 'Nombre debe tener largo de mínimo 3 caracteres.';
    } else {
        valNom.innerText = '';
    }
    if (apell.length < 4) {
        valApell.innerText = 'Apellido debe tener largo de mínimo 4 caracteres.';
    } else {
        valApell.innerText = '';
    }
    if (!emailPattern.test(mail)) { 
        valMail.innerText = 'Formato de correo no válido.';
    } else {
        valMail.innerText = '';
    }
    if (pass.length < 8) {
        valPass.innerText = 'Contraseña debe tener largo de mínimo 8 caracteres.';
    } else {
        valPass.innerText = '';
    }
    if (pass1 !== pass) {
        valPass1.innerText = 'Las contraseñas deben coincidir.';
    } else {
        valPass1.innerText = '';
    }
    if (pass1 === '') {
        valPass1.innerText = 'Por favor, repita la contraseña.';
    }

    if (valNom.innerText === '' && valApell.innerText === '' && valMail.innerText === '' && valPass.innerText === '' && valPass1.innerText === '') {
        alert('Su cuenta ha sido creada.');
    }

    return false;
}