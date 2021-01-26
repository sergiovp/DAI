$(document).ready(function() {
    $('#login').keyup(function() {
        let letrasFormulario = $(this).val();
        let usuarios = Array();

        $.ajax({
            url: `http://localhost:5000/api/usuarios`,
            type : 'GET',
            dataType : 'json',

            success: function(datos) {
                for (let i = 0; i < datos.length; i++) {
                    if (letrasFormulario == datos[i]) {
                        document.getElementById('mensaje_usuario').style.display = 'block';
                        document.getElementById("reg").disabled = true;
                        break;
                    } else {
                        document.getElementById('mensaje_usuario').style.display = 'none';
                        document.getElementById("reg").disabled = false;
                    }
                }
            },

            error: function() {
                console.log("Error");
            }
        });
    });
});