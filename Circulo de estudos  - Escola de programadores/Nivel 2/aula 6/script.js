const body = document.getElementById("corpoSite");
const titulo = document.querySelector("#textoH1");
const botao = document.getElementById("botao");
const lstMenu = document.getElementById("lstMenu");
const background = document.getElementById("background");
let index = 0;
const track = document.getElementById("track");
const slides = document.querySelectorAll(".slide");
const totalSlides = slides.length;


const botaoTeste = () =>{
    titulo.innerText = "Olá Mundo!";

    body.classList.toggle("dark-mode");
}

botao.addEventListener('mouseover', function(){
    titulo.innerText = "Olá Mundo!";

    console.log(body.style.backgroundColor);
    body.classList.toggle("dark-mode");
})

document.getElementById("btnMenu").addEventListener('click', () => {
    lstMenu.classList.toggle("active");
});

window.addEventListener('scroll', () =>{
    requestAnimationFrame(() =>{
        const scroll = window.scrollY;
        background.style.transform = 'translateY(${scroll * 0.5}px)';
    });
});

function updateCarrossel (){
    track.style.transform = `translateX(-${index * 300}px)`;
}


document.getElementById("next").addEventListener('click', () =>{

    console.log(index);
    if (index < totalSlides - 1){
        index++
    } else {
        index = 0;
    }

    updateCarrossel();
});

document.getElementById("prev").addEventListener('click', () =>{

    console.log(index);
    if (index > 0){
        index--
    } else {
        index = totalSlides - 1;
    }

    updateCarrossel();
});

document.querySelector('.caixa').addEventListener('click', () => {
    const timeLine = anime.timeline({
        easing: 'easeOutExpo',
        duration: 750
    });

    timeLine.add({
        targets: '.caixa',
        backgroundColor: '#1aa105',
        rotate: '1turn',
        translateX: 150,
    }).add({
        rotate: '1turn',
        targets: '.caixa',
        backgroundColor: '#a10505',
        translateX: 0,
    });
});