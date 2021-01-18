$(document).ready(function() {
    temaOscuro();

    // PONEMOS MODO OSCURO
    $('#boton-oscuro').click(function () {
        localStorage.setItem('isDarkMode', true);
        temaOscuro();
    });

    // PONEMOS MODO CLARO
    $('#boton-claro').click(function() {
        localStorage.setItem('isDarkMode', false);
        temaOscuro();
    });
});

function temaOscuro() {
    const body = document.body;

    if (!localStorage.getItem('isDarkMode') || localStorage.getItem('isDarkMode') == 'false') {

        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
        }

        document.getElementById('boton-claro').style.display = 'none';
        document.getElementById('boton-oscuro').style.display = 'inline-block';

    } else if (localStorage.getItem('isDarkMode') == 'true') {

        if (!body.classList.contains("dark-mode")) {
            body.classList.add("dark-mode");
        }

        document.getElementById('boton-claro').style.display = 'inline-block';
        document.getElementById('boton-oscuro').style.display = 'none';
    }
}
