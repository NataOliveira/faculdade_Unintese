const track = document.getElementById('track');
const slides = document.querySelectorAll('.slide'); 
const totalSlides = slides.length;
let index = 0;
const titulo = document.getElementById('tituloSite')

function updateCarrossel(){
    track.style.transform = `translateX(-${index * 100}%)`;
}

function avancarSlide() {
    if (index < totalSlides - 1){
        index++;
    } else {
        index = 0;
    }
    updateCarrossel();
}

function voltarSlide() {
    if (index > 0) {
        index--;
    } else {
        index = totalSlides - 1;
    }
    updateCarrossel();
}


document.getElementById('nextDesktop').addEventListener('click', avancarSlide);
document.getElementById('prevDesktop').addEventListener('click', voltarSlide);
document.getElementById('nextMobile').addEventListener('click', avancarSlide);
document.getElementById('prevMobile').addEventListener('click', voltarSlide);



/*---Page_Visibility_API---- */

const audiovolte = document.getElementById('audioVolte')
const audiovoltou = document.getElementById('audioVoltou')
const tituloOriginal = document.title;

document.addEventListener("visibilitychange",() =>{
    if (document.hidden) {
        audiovoltou.pause();
        audiovoltou.currentTime = 0;
        audiovolte.play();
        document.title = 'Volte :c';
    }else{
        audiovolte.pause();
        audiovolte.currentTime = 0;
        audiovoltou.play();
        document.title = tituloOriginal;
    }
})


async function buscarPersonagem(id){
    const url =`https://thesimpsonsapi.com/api/characters/${id}`

    try{
        const resposta = await fetch(url);

        if(!resposta.ok){
            throw new Error(`Erro`)
        }

        const personagem = await resposta.json();

        mostrarPersonagem(personagem);
    } catch (error) {
        console.error("Falha ao buscar dados", error)
    }
}

function mostrarPersonagem(dados){

  const nomePersonagem = document.getElementById('char-nome');
  const profissaoPersonagem = document.getElementById('char-trabalho');
  const frasePersonagem = document.getElementById('char-frase');
  const fotoPersonagem = document.getElementById('char-foto');
  const idadePersonagem = document.getElementById('char-idade');
  const statusPersonagem = document.getElementById('char-status');
  
  nomePersonagem.textContent = dados.name;
  profissaoPersonagem.textContent = `occupation: ${dados.occupation}`;
  idadePersonagem.textContent = `Age: ${dados.age}`;
  statusPersonagem.textContent = `Status: ${dados.status}`

  if (dados.phrases && dados.phrases.length>0) {
    const fraseAleatoria = dados.phrases[Math.floor(Math.random() * dados.phrases.length)];
    frasePersonagem.textContent = `"${fraseAleatoria}"`;

  } else {
    frasePersonagem.textContent = '"..."';
  }

  fotoPersonagem.src = `https://cdn.thesimpsonsapi.com/500${dados.portrait_path}`;
  fotoPersonagem.alt = `Foto de ${dados.name}`
}
buscarPersonagem(1);

let num = 2
document.getElementById('char-foto').addEventListener('click', () => {

    
    buscarPersonagem(num);
    num ++
    
    
})



async function traduzir(texto){

    if (!texto || texto == '"..."') return texto;

    const urlTranslate = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(texto)}&langpair=en|pt-br`;

    try{
        const resposta = await fetch(urlTranslate)
        const dados = await resposta.json()

        return dados.responseData.translatedText;
    } catch (error){
        console.log("Erro ao traduzir",error);
        return texto;   
    }
}

document.querySelector(".btn-traduzir").addEventListener('click', async () => {

    const boxTextoOriginal = document.getElementById("textoOriginal");
    const boxTextoTraduzido = document.getElementById("textoTraduzido");

    const textoTraduzido = boxTextoOriginal.value;

    boxTextoTraduzido.innerText = await traduzir(textoTraduzido);
})



