// Obtém o botão de menu e a sidebar
const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');

// Adiciona um evento de clique no botão para alternar a visibilidade da sidebar
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('active');  // Ativa ou desativa a sidebar
    menuToggle.classList.toggle('active');  // Ativa ou desativa o botão de menu
});

// Fecha a sidebar ao clicar no botão de fechar
const closeBtn = document.querySelector('.sidebar .close-btn');
closeBtn.addEventListener('click', () => {
    sidebar.classList.remove('active');  // Remove a classe active para fechar a sidebar
    menuToggle.classList.remove('active');  // Altera o estado do botão de menu
});

