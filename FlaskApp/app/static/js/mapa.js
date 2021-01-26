function getMapa(latitud = null, longitud = null) {
    /*
        Las coordenadas decimales del lugar y el zoom que se le aplica.
        Cuanto más pequeño el zoom, desde más lejos se ve. El máximo zoom es 18.
        Las coordenadas de Granada son [37.18817, -3.60667].
    */
    var mymap = L.map('mapid').setView([40.4165, -3.70256], 6);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: '',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoidmVsYTk2IiwiYSI6ImNra2EwdzA0cTBvMTEycXM5ZjVvcDVma3kifQ.V_7W1o8NfzV1Us7-aDkwbQ'
    }).addTo(mymap);

    if (latitud != -1 && longitud != -1) {
        var circle = L.circle([latitud, longitud], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: 50000
        }).addTo(mymap).on('click', function () {
           // Consulta API con todos los Pokémon
           $(document).ready(function() {        
                $.ajax({
                    url: `http://localhost:5000/api/ubicacion?longitud=${longitud}`,
                    type : 'GET',
                    dataType : 'json',
        
                    success: function(datos) {
                        let HTMLMostrar = '<h4 style="text-align: center;"> Estos son los Pokémon que podemos encontrar en esa zona: </h4>';
                        HTMLMostrar += '<div class="container" style="text-align: center;"><div id="pk">';
                        for (let i = 0; i < datos.length; i++) {
                            if (i % 2 == 0) {
                                HTMLMostrar += '<div class="pokemon-pares"><div class="colum">';
                                HTMLMostrar += `<img src="${datos[i].img}" alt="">`;
                                HTMLMostrar += `<p>${datos[i].numero} | ${datos[i].nombre}</p></div></div>`;
                            } else {
                                HTMLMostrar += '<div class="pokemon-impares"><div class="colum">';
                                HTMLMostrar += `<img src="${datos[i].img}" alt="">`;
                                HTMLMostrar += `<p>${datos[i].numero} | ${datos[i].nombre}</p></div></div>`;
                            }
                        }
                        HTMLMostrar += '</div></div>';
                        document.getElementById("mostrar-pokemon").innerHTML = HTMLMostrar;
                    },
        
                    error: function() {
                        console.log("Error");
                    }
                });
            }); 
        });
    } else {
        window.setInterval (parpadea, 500);
        var color = "red";

        function parpadea () {
            let brilla = document.getElementById ("pokemon-desconocido");

            if (localStorage.getItem('isDarkMode') == 'true') {
                color = (color == "#ffffff")? "red" : "#ffffff";
                brilla.style.color = color;
                brilla.style.fontSize='36px';
            } else {
                color = (color == "#000000") ? "red" : "#000000";
                brilla.style.color = color;
                brilla.style.fontSize='36px';
            }
        }
        document.getElementById('pokemon-desconocido').innerHTML = "<h1>¡UBICACIÓN DESCONOCIDA!</h1>";
    }
}

function getLatitud() {
    return document.getElementById('latitud').innerHTML;
}

function getLongitud() {
    return document.getElementById('longitud').innerHTML;
}
