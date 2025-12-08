const chair1 = document.querySelector('#chair1');
const chair2 = document.querySelector('#chair2');
const chair3 = document.querySelector('#chair3');


window.addEventListener('scroll', () => {
    let value = scrollY;
    chair1.style.rotate = `${value}deg`;
    chair2.style.rotate = `${value * 2}deg`;
    chair3.style.rotate = `${value * 3}deg`
})
