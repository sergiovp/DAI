function temaOscuro() {
    var body = document.body;

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
