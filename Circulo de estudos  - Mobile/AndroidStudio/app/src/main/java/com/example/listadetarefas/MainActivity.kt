package com.example.listadetarefas

import android.app.Activity
import android.os.Bundle
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.listadetarefas.modelos.Tarefas

class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        val recyclerView = findViewById<RecyclerView>(R.id.reciclerView)

        val tarefas = listOf(
            Tarefas(
                nome = "Jogar",
                descricao = "Jogar Truco",
                hora = "20:00h"
            ),
            Tarefas(
                nome = "Conversar",
                descricao = "Falar muita besteira",
                hora = "22:00h"
            )
        )

        recyclerView.adapter = ListaDeTarefasAdapter(tarefas, this)

    }

}