# Labirinto do Minotauro - Busca Greedy e A*

Este projeto implementa algoritmos de busca **Greedy** e **A*** para encontrar caminhos em labirintos representados como grafos. O usuário pode definir limites opcionais de comprimento de fio para a busca.

---

## Pré-requisitos

- Python 3.10 ou superior

## Estrutura do projeto

```bash
projeto-2
├── algorithms/
│   └── __init__.py
│   ├── a_search.py
│   └── greedy_search.py
├── examples/
│   └── maze00.txt
│   └── maze01.txt
│   └── maze02.txt
│   └── maze03.txt
│   └── maze04.txt
│   └── maze05.txt
│   └── maze06.txt
├── schemas/
│   └── __init__.py
│   └── graph.py
├── utils/ 
│   └── __init__.py
│   └── graph.py
│   └── view.py
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
├── run_tests.sh
└── uv.lock

```

## Executando o projeto

Você pode executar o script principal (`main.py`) usando `py` (Windows) ou `python3` (Linux):

### Windows

```bash
py main.py --file <CAMINHO_DO_ARQUIVO> [--alg {greedy,a_star}] [--wire <COMPRIMENTO_DO_FIO>]
```

### Linux

```bash
python3 main.py --file <CAMINHO_DO_ARQUIVO> [--alg {greedy,a_star}] [--wire <COMPRIMENTO_DO_FIO>]
```

### Argumentos

- `--file` (**Obrigatório**): Caminho do arquivo de entrada do grafo/labirinto
- `--alg` (**Opcional**): Algoritmo a ser usado: `greedy` ou `a_star`. Se não for informado, será solicitado interativamente
- `--wire` (**Opcional**): Define o comprimento do fio para a busca. Se não informado, será solicitado interativamente

## Exemplos de execução

### Executando `greedy` com limite de fio

```bash
python3 main.py --file examples/maze02.txt --alg greedy --wire 10
```

### Executando `a_star` sem limite de fio

Neste caso, será perguntando ao usuário iterativamente se deseja adicionar uma condição de fio ou não; se sim, será perguntado o tamanho do fio

```bash
python3 main.py --file examples/maze02.txt --alg a_star
```

### Executando sem algoritmo e fio

Neste caso, será perguntando ao usuário iterativamente tanto o algoritmo quanto se deseja adicionar uma condição de fio ou não; se sim, será perguntado o tamanho do fio

```bash
python3 main.py --file examples/maze02.txt
```

## Saída esperada

A cada iteração será mostrado ao usuário qual iteração que está, os elementos que estão na fronteira e a medida de desempenho (nós expandidos).

```bash
Iteração: <ITERAÇÃO>
Lista: <LISTA_DE_ELEMENTOS_NA_FRONTEIRA>
Medida de desempenho: <NUMERO_DE_NOS_EXPANDIDOS>
```

Ao final, será apresentado ao usuário um resumo da busca no labirinto, mostrando a distância percorrida, o caminho e a medida de desemenho.

```bash
Distância: <DISTANCIA_PERCORRIDA>
Caminho: <CAMINHO_ATE_O_NO_FINAL>
Medida de desempenho: <NUMERO_DE_NOS_EXPANDIDOS>
```

Se não houver caminho possível, será exibido

```bash
Distância: inf # Infinito
Caminho: inexistente
Medida de desempenho: <NUMERO_DE_NOS_EXPANDIDOS>
```
