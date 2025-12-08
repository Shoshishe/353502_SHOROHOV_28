const themeToggle = document.getElementById('theme-toggle');
const theme = localStorage.getItem('theme') || 'dark';

function setTheme(theme) {
    if (theme === 'light') {
        document.body.classList.remove('dark');
    } else {
        document.body.classList.add('dark')
    }
    localStorage.setItem('theme', theme)
}

setTheme(theme);

themeToggle.addEventListener('click', () => {
    const currentTheme = localStorage.getItem('theme')
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
});