$(document).ready(function() {

    // Al introducir caracteres en el buscador
    $('#buscar').keyup(function() {
        let letrasFormulario = $(this).val();

        $.ajax({
            // Petición a la API, obtenemos los Pokémon cuyo nombre coincida con el introducido
            url: `http://localhost:5000/api/filtro_pokemon?name=${letrasFormulario}`,
            type : 'GET',
            dataType : 'json',

            success: function(datos) {
                let HTMLMostrar = getHTML(datos, letrasFormulario);
                document.getElementById("txt").innerHTML = HTMLMostrar;
            },

            error: function() {
                let HTMLMostrar = errorLetras(letrasFormulario);
                document.getElementById("txt").innerHTML = HTMLMostrar;
            }
        });
    });
});

function errorLetras(letrasFormulario) {
    let HTMLMostrar = '';

    if (letrasFormulario) {
        HTMLMostrar = `<h4 style="color:red; text-align: center;"> No se encontró información para '${letrasFormulario}'.</h3>`;
    }
    return HTMLMostrar;
}

function getHTML(datos, letrasFormulario) {
    let HTMLMostrar = '<div class="container" style="text-align: center;"><div class="row">';
    let pares = false;
    $.each(datos, function (i, valor) {
        if (pares) {
            HTMLMostrar += '<div class="pokemon-pares"><div class="colum">';
            pares = false;
        } else {
            HTMLMostrar += '<div class="pokemon-impares"><div class="colum">';
            pares = true;
        }

        HTMLMostrar += `<img src="${valor.img}">`;
        HTMLMostrar += `<p>${valor.numero} | ${valor.nombre}</p>`;
        HTMLMostrar += `<p><a role="button" onclick="eliminar('${valor.id}', '${letrasFormulario}')">Eliminar</a></p>`;
        HTMLMostrar += '</div></div>';
    });
    
    HTMLMostrar += '</div></div>';
    
    return HTMLMostrar;
}

function eliminar(id, letrasFormulario) {
    $(function () {

        $.ajax({
            url: `http://localhost:5000/api/del_pokemon/${id}`,
            type : 'DELETE',
            dataType : 'json',

            success: function() {
                $.ajax({
                    url: `http://localhost:5000/api/filtro_pokemon?name=${letrasFormulario}`,
                    type : 'GET',
                    dataType : 'json',

                    success: function(datos) {
                        let HTMLMostrar = getHTML(datos, letrasFormulario);
                        document.getElementById("txt").innerHTML = HTMLMostrar;
                    },

                    error: function() {
                        let HTMLMostrar = errorLetras(letrasFormulario);
                        document.getElementById("txt").innerHTML = HTMLMostrar;
                    }
                });
            },

            error: function() {
                let HTMLMostrar = `<h4 style="color:red; text-align: center;"> No se pudo eliminar el Pokémon.</h3>`;
                document.getElementById("txt").innerHTML = HTMLMostrar;
            }
        });
    });
}
