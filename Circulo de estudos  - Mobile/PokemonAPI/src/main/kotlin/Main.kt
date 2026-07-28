import com.google.gson.Gson
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.net.http.HttpResponse.BodyHandlers
import java.util.*


fun main(){

    val leitor = Scanner(System.`in`)

    print("Digite um ID: ")
    val buscador = leitor.nextLine()

    val client : HttpClient = HttpClient.newHttpClient()

    val request = HttpRequest.newBuilder()
        .uri(URI.create("https://pokeapi.co/api/v2/pokemon/$buscador"))
        .build()

    val response = client.send(request, HttpResponse.BodyHandlers.ofString())

    val dados = response.body()

    val gson = Gson()

    val buscaAPI = gson.fromJson(dados, Informacoes::class.java)

    val meuPokemon = Pokemon(buscaAPI.name, buscaAPI.abilities)

    println(meuPokemon.nome.replaceFirstChar{it.uppercase()})
    println("HABILIDADES")
    for (i in meuPokemon.habilidades)
        println(i.ability.name.replaceFirstChar { it.uppercase() })
    println(" | ")




}