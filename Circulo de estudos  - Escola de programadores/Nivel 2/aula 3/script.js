let x = 0;
let y = 0;
let resultado = 0;

resultado = x+y;

console.log(resultado);

if ((x == 0) || (y == 0)){
    console.log('zerou');
}



let vet = [3,5,2,3,4,6];
soma = 0;
for (let cont = 0; cont <= 10; cont ++){
    for (let cont2 = 0; cont2 <=10; cont2 ++){
        console.log(`${cont} X ${cont2} = ${cont*cont2}`)
    }
}



/* While*/
contador = 0;
while (contador <= 10){
    console.log(contador);
    contador ++
}


/*DO While*/
contador = 0
do {
    console.log(contador)
    contador ++
}   while( contador <= 0)


/*Funções*/


const somar = function(a, b){
    return ((a + b));
}
console.log(somar(2, 3));

/*Funções arrior*/


const subt = (a ,b) => a - b;
console.log(subt(7, 3));

