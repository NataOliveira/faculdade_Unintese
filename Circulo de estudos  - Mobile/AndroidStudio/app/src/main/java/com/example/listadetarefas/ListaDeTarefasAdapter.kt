package com.example.listadetarefas

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.listadetarefas.modelos.Tarefas



class ListaDeTarefasAdapter(
    val tarefas: List<Tarefas>,
    val contexto: Context
): RecyclerView.Adapter<ListaDeTarefasAdapter.ListaTarefasViewHolder>() {

    class ListaTarefasViewHolder(view : View): RecyclerView.ViewHolder(view) {
        fun unir(tarefas: Tarefas){

            val nome = itemView.findViewById<TextView>(R.id.nome)
            nome.text = tarefas.nome

            val descricao = itemView.findViewById<TextView>(R.id.descricao)
            descricao.text = tarefas.descricao
            val hora = itemView.findViewById<TextView>(R.id.hora)
            hora.text = tarefas.hora
        }
    }

    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): ListaTarefasViewHolder {

        val inflador = LayoutInflater.from(contexto)
        val view = inflador.inflate(R.layout.tarefa_individual,parent, false )

        return ListaTarefasViewHolder(view)
    }

    override fun onBindViewHolder(
        holder: ListaTarefasViewHolder,
        position: Int
    ) {
        val tarefa = tarefas[position]
        holder.unir(tarefa)

    }

    override fun getItemCount(): Int {
        return tarefas.size
    }
}