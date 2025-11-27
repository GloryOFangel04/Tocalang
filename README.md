# TocaLang 🐇

> "A porta de entrada para o seu universo de descobertas na programação."

**TocaLang** é uma linguagem de programação desenvolvida com o intuito de ser simples e acessível, utilizando a língua portuguesa como base para tornar a confecção do código mais natural e intuitiva.

## 📖 Sobre o Projeto

O intuito deste documento e do projeto é demonstrar como criar programas utilizando a TocaLang, além de detalhar o processo de confecção de cada funcionalidade do compilador.

A linguagem foi projetada para reduzir a barreira de entrada na lógica de programação, permitindo que o usuário foque no algoritmo sem se preocupar excessivamente com sintaxes complexas em inglês no início do aprendizado.

### 💡 Por que "TocaLang"?

O nome teve como inspiração o conceito de *"Rabbit Hole"* (Toca do Coelho) do clássico literário *Alice no País das Maravilhas*.

Na obra, a toca não é apenas um buraco, mas o portal de passagem que leva a protagonista do mundo comum para um universo de descobertas fascinantes. Escolhemos esse nome para simbolizar que esta linguagem é a porta de entrada acessível para quem deseja mergulhar na lógica da programação.

---

## 🛠️ Arquitetura e Desenvolvimento

O compilador da TocaLang foi desenvolvido utilizando as seguintes tecnologias:

* **ANTLR4:** Utilizado para a definição da gramática e análise léxica/sintática.
* **Python:** Linguagem anfitriã utilizada para a lógica do compilador.

### Como funciona
Na parte de controle, foi implementado o padrão de projeto **Visitor** junto a classes auxiliares em Python. Essa estrutura percorre a árvore sintática gerada pelo ANTLR4 e executa as ações correspondentes a cada comando da TocaLang.

---

## 🚀 Como Executar

O compilador foi projetado para ser flexível quanto à extensão dos arquivos de código fonte.

### Extensões Suportadas
* **`.toca`** (Recomendado): A extensão oficial da linguagem, criada para fins estéticos e de identificação.
* **`.txt`**: Arquivos de texto comum também são aceitos.

> **Nota:** O compilador lê ambos os formatos (`.toca` e `.txt`) da mesma maneira, sem perda de funcionalidades ou desempenho entre eles.

### Pré-requisitos
* Python 3.x instalado.
* Runtime do ANTLR4 para Python (`pip install antlr4-python3-runtime`).

### Rodando um programa
Para executar um arquivo, utilize o seguinte comando no seu terminal:

```bash
python main.py seu_programa.toca
