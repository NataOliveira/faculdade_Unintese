
const titulo = document.getElementById("textoH1")
const body = document.getElementById("body")
const botaotema = document.getElementById("botaotema")
const botaoTeste = () =>{
    titulo.innerText = "Olá Mundo!";
    }

const botaoTheme = () =>{
  console.log(body.style.backgroundColor)

   body.classList.toggle ("dark-mode");

}