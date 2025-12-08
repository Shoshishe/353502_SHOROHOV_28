window.addEventListener('load', function () {
    const preloader = document.getElementById('preloader')
    const content = document.getElementById('content')

    preloader.style.opacity = 0;
    preloader.style.display = 'none';
    content.style.display = 'block';
})