let loop, nav, pags, auto, stopMouseHover;
nav = loop = pags = auto = stopMouseHover = true;
let delay = 1;

const slider = document.querySelector('.slider-container')
let prevButton = document.querySelector('.prev-button')
let nextButton = document.querySelector('.next-button')
prevButton.addEventListener('click', showPreviousSlide);
nextButton.addEventListener('click', showNextSlide);

const sliderCount = document.querySelector('.slider-count')
const slides = Array.from(slider.querySelectorAll('figure'));
const slidesCount = slides.length;
let slideIndex = 0;

let nextSlide = window.setInterval(() => {
    showNextSlide();
}, delay * 1000)

function addHoverEvent() {
    slider.addEventListener('mouseenter', removeInterval);
    slider.addEventListener('mouseleave', addInterval)
}

function removeInterval() {
    window.clearInterval(nextSlide)
}

function addInterval() {
    if (auto) {
        nextSlide = window.setInterval(() => {
            showNextSlide();
        }, delay * 1000);
    }
}

function reapplyHover() {
    window.clearInterval(nextSlide)
    nextSlide = window.setInterval(() => {
        showNextSlide();
    }, delay * 1000)
}

function showPreviousSlide() {
    if (loop) {
        bullets[slideIndex].classList.remove('active');
        slideIndex = (slideIndex - 1 + slidesCount) % slidesCount;
        bullets[slideIndex].classList.add('active');
    } else {
        bullets[slideIndex].classList.remove('active');
        slideIndex = (slideIndex - 1) > 0 ? slideIndex - 1 : 0;
        bullets[slideIndex].classList.add('active');
    }
    updateSlider();
}
function showNextSlide() {
    if (loop) {
        bullets[slideIndex].classList.remove('active');
        slideIndex = (slideIndex + 1) % slidesCount;
        bullets[slideIndex].classList.add('active');
    } else {
        bullets[slideIndex].classList.remove('active');
        slideIndex = (slideIndex + 1) < slidesCount - 1 ? slideIndex + 1 : slidesCount - 1;
        bullets[slideIndex].classList.add('active');
    }
    updateSlider();
}

function updateSlider() {
    slides.forEach((slide, index) => {
        if (index === slideIndex) {
            sliderCount.innerHTML = `${index + 1} / ${slidesCount}`
            slide.style.display = 'block';
        } else {
            slide.style.display = 'none';
        }
    });
}

let bullets = document.querySelector('#slider-pag').querySelectorAll('.dot');

function addPagination() {
    bullets.forEach((bullet, i) => {
        bullet.addEventListener('click', paginationCallback(i));
    });
}

function paginationCallback(index) {
    return function () {
        slideIndex = index;
        slides.forEach((slide, index) => {
            if (index === slideIndex) {
                sliderCount.innerHTML = `${index + 1} / ${slidesCount}`
                slide.style.display = 'block';
                bullets[index].classList.add('active');
            } else {
                bullets[index].classList.remove('active');
                slide.style.display = 'none';
            }
        });
    }
}

updateSlider();
addHoverEvent();
addPagination();

const checkboxesContainter = document.querySelector('.slider-ck');

checkboxesContainter.querySelector("#nav-ck").addEventListener('change', function (event) {
    if (!event.target.checked) {
        prevButton.style.display = 'block';
        nextButton.style.display = 'block';
        nav = true;
    } else {
        nav = false;
        prevButton.style.display = 'none';
        nextButton.style.display = 'none';
    }
});

checkboxesContainter.querySelector("#pag-ck").addEventListener('change', function (event) {
    if (event.target.checked) {
        bullets.forEach((bullet) => {
            bullet.style.display = 'none';
        });
    } else {
        bullets.forEach((bullet) => { bullet.style.display = "inline-block" });
    }
});

checkboxesContainter.querySelector("#loop-ck").addEventListener('change', function (event) {
    loop = event.target.checked ? false : true;
});

checkboxesContainter.querySelector("#auto-ck").addEventListener('change', function (event) {
    if (event.target.checked) {
        auto = false;
        window.clearInterval(nextSlide);
    } else {
        auto = true;
        nextSlide = window.setInterval(() => {
            showNextSlide();
        }, delay * 1000);
    }
    auto = event.target.checked ? false : true;
});

checkboxesContainter.querySelector('#stopMouseHover-ck').addEventListener('change', function (event) {
    if (event.target.checked) {
        slider.removeEventListener('mouseenter', removeInterval);
        slider.removeEventListener('mouseleave', addInterval);
    } else {
        addHoverEvent();
    }
})


checkboxesContainter.querySelector("#delay-ck").addEventListener('change', function (event) {
    delay = parseFloat(event.target.value);
    if (auto) {
        reapplyHover();
    }
});
