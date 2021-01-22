$(document).ready(function() {
    $('#login').keyup(function() {
        let letrasFormulario = $(this).val();
        let usuarios = Array();

        var usua = document.getElementsByClassName("usuarios");
        for (let i = 0; i < usua.length; i++) {
            usuarios.push(document.getElementsByClassName("usuarios")[i].innerHTML);
        }

        for (let i = 0; i < usuarios.length; i++) {
            if (letrasFormulario == usuarios[i]) {
                document.getElementById('mensaje_usuario').style.display = 'block';
                break;
            } else {
                document.getElementById('mensaje_usuario').style.display = 'none';
            }
        }
    });
});