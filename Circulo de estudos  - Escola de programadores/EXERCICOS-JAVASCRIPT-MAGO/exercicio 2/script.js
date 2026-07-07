const resultado = document.getElementById("resultado");
function pegarValor() {
    return Number(document.getElementById("inputNum").value);
}

const tabuada = () =>{
    
    let valorInserido = pegarValor();
    let tabuadaresultado = [];

    if (valorInserido >= 1){
        for (let cont = 1; cont <= 10; cont ++){
            tabuadaresultado.push(`${valorInserido} X ${cont} = ${valorInserido*cont}`);   
            resultado.innerText = tabuadaresultado.join("\n");
    }
}
    else{
        resultado.innerText = "Número inválido !";
    }
}
    
/*Botao 2*/
const numerosPares = () => {
    let valorInserido = pegarValor();
    let numerospareslista= [];
    if (valorInserido >= 1){
        for (let cont = 1; cont <= valorInserido; cont++){
        if(cont % 2 === 0) {
            numerospareslista.push(cont);
        }
    }
        resultado.innerText = numerospareslista.join(", ");
    }
    
    else{
        resultado.innerText = "Número inválido !";
    }

}
/*Botao 3*/
const somaIntervalo = () => {
    let valorInserido = pegarValor();
    let somatotal = 0;

    if (valorInserido >= 1){
        while (valorInserido >= 0){
            somatotal += valorInserido;
            valorInserido --;
        }
        resultado.innerText = somatotal;
    }
    else{
        resultado.innerText = "Número inválido !";
    }

}

/*Botao 4*/
const fatorial = () => {
    let valorInserido = pegarValor();
    let fatorial = 1;

    if (valorInserido >= 1){
        while (valorInserido > 0){
            fatorial = fatorial * valorInserido;
            valorInserido--;
}
        resultado.innerText = fatorial;
    }
    else{
        resultado.innerText = "Número inválido !";
    }
}

/*Botao 5*/
const validarPrimo = () => {
    let valorInserido = pegarValor();
    let contador_de_divisiveis = 0;


    for (let cont = valorInserido; cont > 0; cont--){

        if (valorInserido % cont == 0){
            contador_de_divisiveis += 1
        }
    }
    /*Valida se o número é divisivel por mais de duas vezes (1 e ele mesmo), se sim irá printar que é primo, senão irá printar que não é*/
    if (valorInserido > 1 && contador_de_divisiveis == 2){
        resultado.innerText = valorInserido + " é um número primo";
    }
    else{
        resultado.innerText = valorInserido + " não é um número primo";

    }
}

/*Um objeto com as funçoes*/
const operacoes = {
    tabuada: tabuada,
    pares: numerosPares,
    soma: somaIntervalo,
    fatorial: fatorial,
    primo: validarPrimo
};

/*--------------------------EventListeners ----------------------------*/

/*Pega todos os botões e conecta o evento de clique, quando cliclado executa a funções correspondente da data-operacao*/
document.querySelectorAll(".btn").forEach((botao) => {
    botao.addEventListener("click", () => {
        const operacao = botao.dataset.operacao;
        operacoes[operacao]();
    });
});

/*Copia o resultado com um clique*/
resultado.addEventListener("click", () => {
    navigator.clipboard.writeText(resultado.innerText);
    resultado.style.opacity = "0.5";
    setTimeout(() => resultado.style.opacity = "1", 200);
});

/*Limpa o resultado quando digitar no input */
document.getElementById("inputNum").addEventListener("input", () => {
    resultado.innerText = "";
});


