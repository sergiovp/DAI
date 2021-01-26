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
                        break;
                    } else {
                        document.getElementById('mensaje_usuario').style.display = 'none';
                    }
                }
            },

            error: function() {
                console.log("Error");
            }
        });
    });
});