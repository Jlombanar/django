document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        var mensaje = document.querySelector(".messages");
        if (mensaje) {
            mensaje.style.display = "none"; 
            window.location.href = "/"; 
        }
    }, 5000); 
});