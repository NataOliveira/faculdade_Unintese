let array = [1,2,3,4,5]

/**Mapeia cada indice e manipula ele */
let dobro = array.map(num => num * 2 );


console.log(dobro)



/**Mapeia cada indice e valida se é True ou False */
let par= array.filter(num => num % 2 === 0)

console.log(par);


/**Reduz todos os valores do array para um único valor */
let som = array.reduce((x,y) => {

    return x + y
}, 0)

console.log(som)

