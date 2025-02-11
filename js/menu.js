const burgerMenu = document.getElementById('burger-menu');
const nav = document.getElementById('nav');

burgerMenu.addEventListener('click', () => {
    // Toggle (ein-/ausblenden) des Navigationsmenüs
    nav.style.display = nav.style.display === 'block' ? 'none' : 'block';
});
