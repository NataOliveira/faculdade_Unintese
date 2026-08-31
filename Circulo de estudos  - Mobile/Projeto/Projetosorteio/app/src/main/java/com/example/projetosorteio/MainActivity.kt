package com.example.projetosorteio

import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)

        val participantes = listOf(
            "João",
            "Maria",
            "Pedro",
            "Sara",
            "Ana",
            "Henrique",
            "Adriano",
            "Ester",
            "Yasmin",
            "Amara",
            "José",
            "Antonio",
            "Paulo",
            "Vanessa"
        )

        val recyclerView =
            findViewById<RecyclerView>(R.id.recyclerView)

        val botaoSorteio =
            findViewById<Button>(R.id.botaoSorteio)

        val adapter = VencedorAdapter(emptyList())

        recyclerView.layoutManager =
            LinearLayoutManager(this)

        recyclerView.adapter = adapter

        botaoSorteio.setOnClickListener {

            val vencedores =
                participantes.shuffled().take(1)

            adapter.atualizarLista(vencedores)
        }
    }
}