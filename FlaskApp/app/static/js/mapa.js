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

    var circle = L.circle([latitud, longitud], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 600
    }).addTo(mymap);
}

function getLatitud() {
    return document.getElementById('latitud').innerHTML;
}

function getLongitud() {
    return document.getElementById('longitud').innerHTML;
}
