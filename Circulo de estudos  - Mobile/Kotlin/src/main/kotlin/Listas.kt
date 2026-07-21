//fun listas() {
//    val listaMutavel: MutableList<String> = mutableListOf("Natan")
//    val listaImutavel: List<String> = listOf("natan")
//}



fun main(){

    println("Digite num: ")
    val nota = readln()?.toDoubleOrNull() ?: 0.0

    if (nota < 6) {
        println("jamanta")
    } else{
        println("passou")
    }


    val lista: List<String> = listOf("A", "B", "C", "D")

    lista.forEach {(
            println("letra: $it")

    )}

}
