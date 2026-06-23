# ⚔️ CLI RPG Game - Jornada dos Heróis

Um jogo de RPG baseado em turnos executado diretamente no terminal, desenvolvido em **Python**. O projeto aplica conceitos fundamentais de **Programação Orientada a Objetos (POO)**, herança, polimorfismo e manipulação de fluxos de controle estruturados em laços de repetição.

---

## 🎮 Como Jogar

1. **Seleção de Classe e Herói**: Escolha entre três arquétipos clássicos: **Soldado**, **Mago** ou **Atirador**. Cada classe possui três heróis históricos/fictícios com atributos únicos de HP, Ataque, Defesa e Dano Ultimate.
2. **Ciclo de Batalhas**: Enfrente hordas de monstros que evoluem conforme sua experiência aumenta.
3. **Fases do Jogo**:
   * **Até 100 XP**: Mobs Fracos (Goblins, Zumbis, etc.) + Chefe da Fase.
   * **Level Up**: Transição de fase com desbloqueio de criaturas de Elite.
   * **Até 200 XP**: Mobs de Elite (Orcs, Trolls, etc.) + Boss Final.
4. **Mecânica de Turnos**: A cada turno, decida entre atacar, usar sua habilidade definitiva (*Ultimate*) ou gerenciar seu inventário de poções coletadas.

---

## 🛠️ Estrutura do Código (Arquitetura POO)

O projeto está dividido modularmente para garantir organização e escalabilidade:

### 🧱 Classe Base (`BaseChar`)
A espinha dorsal de todas as entidades do jogo (Heróis e Monstros). Controla atributos principais e métodos globais de combate e itens:
* `atacar(oponente)` / `ultimate(oponente)`
* `ganhar_xp(oponente)`
* `drop_items(hero)` (Gerencia o loot aleatório de poções alquímicas)
* `abrir_inventario()` (Exibe a contagem dinâmica de poções categorizadas por tamanho)

### 🛡️ Heróis (Subclasses de `BaseChar`)
* **Soldado**: Especialistas em combate corpo a corpo. Contém heróis como *Aquiles*, *Joana d'Arc* e *Leônidas*.
* **Mago**: Manipuladores de energia arcana com controle de recurso de Mana. Contém *Merlin*, *Morgana* e *Gandalf*.
* **Atirador**: Causadores de dano à distância com alta precisão. Contém *Fallen*, *Garrus* e *Karl*.

### 👾 Criaturas (Subclasses de `BaseChar`)
* **MobFraco**: Inimigos iniciais para ganho rápido de experiência.
* **MobElite**: Desafios intermediários com escalonamento de vida e armadura.
* **Boss**: Chefes de fase com ataques personalizados e alto poder destrutivo.

---

## 📂 Organização dos Arquivos

```text
├── main.py              # Fluxo principal do jogo (Laço de gameplay)
├── functions.py         # Funções auxiliares (Spawners, seletores e menus)
└── char/                # Pacote contendo os módulos dos personagens
    ├── __init__.py      # Inicializador do pacote de personagens
    ├── base_char.py     # Classe abstrata/base BaseChar
    ├── herois/          # Classes e instâncias dos heróis (Soldado, Mago, Atirador)
    └── mobs/            # Classes e instâncias dos inimigos (Fraco, Elite, Boss)