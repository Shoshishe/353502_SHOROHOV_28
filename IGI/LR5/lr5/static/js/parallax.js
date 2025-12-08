const body = document.querySelector('body');
const article = document.querySelector('.parallax-container');
const walk = { x: 20, y: 15 };

function parallax(element) {
      const width = article.offsetWidth;
      const height = article.offsetHeight;

      const xWalk = Math.round((element.x / width / 2 * walk.x) - (walk.x / 2));
      const yWalk = Math.round((element.y / height / 2 * walk.y) - (walk.y / 2));

      article.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
}

body.addEventListener('mousemove', parallax);
