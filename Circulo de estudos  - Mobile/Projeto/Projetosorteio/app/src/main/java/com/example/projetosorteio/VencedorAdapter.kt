package com.example.projetosorteio

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class VencedorAdapter(
    var vencedores: List<String>
) : RecyclerView.Adapter<VencedorAdapter.ViewHolder>() {

    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val textVencedor: TextView =
            view.findViewById(R.id.textVencedor)
    }

    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): ViewHolder {

        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_vencedor, parent, false)

        return ViewHolder(view)
    }

    override fun onBindViewHolder(
        holder: ViewHolder,
        position: Int
    ) {
        holder.textVencedor.text =
            "Vencedor ${position + 1}: ${vencedores[position]}"
    }

    override fun getItemCount(): Int {
        return vencedores.size
    }

    fun atualizarLista(novosVencedores: List<String>) {
        vencedores = novosVencedores
        notifyDataSetChanged()
    }
}