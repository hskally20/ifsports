// Obtém o botão de menu e a sidebar
const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');

// Adiciona um evento de clique no botão para alternar a visibilidade da sidebar
$(document).ready(function () {
    // Alterna a classe 'active' na sidebar
    $('.menu-toggle').click(function () {
        $('.sidebar').toggleClass('active');
        $(this).toggleClass('active');  // Adiciona ou remove a classe 'active' no botão de menu
    });

    // Fecha a sidebar quando o botão de fechar for clicado
    $('.close-btn').click(function () {
        $('.sidebar').removeClass('active');
    });
});
