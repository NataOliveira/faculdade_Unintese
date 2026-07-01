/* Cria função de input(), usando a biblioteca prompt-sync ( npm install prompt-sync) */
const ps = require("prompt-sync");
const input = ps();

/* Cria função de print(), que fará um print do parametro, somente para facilitar o desenvolvimento do código*/
function print(x){
    console.log(x);
}

// /*--------------------------- *Exercício 1 ----------------------------------------- */
// /*Tabuada Personalizada: Peça ao usuário um número e exiba a tabuada de 1 a 10 desse valor em uma única saída ou linha por linha */

print('\nExercício 1 - Tabuada Personalizada\n');

let numero =  parseInt(input('digite um numero:  '));

print('\nResultado:\n')
/*Laço onde criará a tabuada*/
for (let cont = 1; cont <= 10; cont ++){
    print(`${numero} X ${cont} = ${numero*cont}`);
    
}

/*--------------------------- *Exercício 2 ----------------------------------------- */
/*Números Pares: Solicite um número e exiba apenas os números pares entre 1 e o valor informado*/

print('\nExercício 2 - Números Pares\n');

numero =  parseInt(input('digite um numero:  '));

/*Laço onde mostrará somente os numeros pares de 1 ao número inserido*/
for (let cont = 1; cont <= numero; cont++){
    if(cont % 2 === 0) {
        print(`${cont}`);
    }
}


/*--------------------------- *Exercício 3 ----------------------------------------- */
/*Soma de Intervalo: Crie um programa que calcule a soma de todos os números inteiros de 1 a 100 (ou até um número n digitado pelo usuário) */

print('\nExercício 3 - Soma de Intervalo\n');

numero =  parseInt(input('digite um numero:  '));
somatorio = 0;

/*Laço onde somará todos os números de 0 ao número inserido*/
while (numero >= 0){
   somatorio += numero;
   numero --;
}
print(somatorio);


/*--------------------------- *Exercício 4 ----------------------------------------- */
/*Cálculo de Fatorial: Peça um número e calcule o seu fatorial (ex: 5!=5×4×3×2×1=120) utilizando um laço de repetição antes de introduzir o conceito de recursividade*/

print('\nExercício 4 - Cálculo de Fatorial\n');
numero =  parseInt(input('digite um numero:  '));
fatorial = 1;

/*Laço onde irá calcular o fatorial do número inserido */
while (numero > 0){
   fatorial = fatorial * numero;
   numero--;
}
print(fatorial);

/*--------------------------- *Exercício 5 ----------------------------------------- */
/*Verificador de Números Primos: O programa deve receber um número e verificar se ele possui divisores além de 1 e dele mesmo*/

print('\nExercício 5 - Verificador de Números Primos\n');

numero =  parseInt(input('digite um numero:  '));
contador_de_divisiveis = 0;

/*Laço onde irá verificar quantas vezes o númeor foi devisivel por outro */
for (let cont = numero; cont > 0; cont--){

    if (numero % cont == 0){
        contador_de_divisiveis += 1
    }
}
/*Valida se o número é divisivel por mais de duas vezes (1 e ele mesmo), se sim irá printar que é primo, senão irá printar que não é*/
if (numero > 1 && contador_de_divisiveis == 2){
    print(`${numero} É um número primo`);
}
else{
    print(`${numero} Não um número primo`);
}