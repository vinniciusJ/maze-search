import argparse
import sys

from utils.graph import parse_graph_from_file
from algorithms.a_search import a_search_start
from algorithms.greedy_search import greedy_search_start
from schemas.graph import MazeSearchResult, Graph, HeapMap


def parse_args() -> argparse.Namespace:
    """
    Define e processa os argumentos de linha de comando.

    Args:
        None

    Returns:
        argparse.Namespace: Objeto contendo os argumentos processados:
            - file (str): Caminho do arquivo de entrada.
            - alg (str | None): Algoritmo selecionado ('greedy' ou 'a_star').
            - wire (int | None): Comprimento do fio (opcional).
    """
    parser = argparse.ArgumentParser(
        description="Busca no labirinto do Minotauro (Greedy e A*)."
    )

    parser.add_argument("--file", required=True, help="Caminho do arquivo de entrada.")

    parser.add_argument(
        "--alg",
        choices=["greedy", "a_star"],
        help="Algoritmo a executar.",
    )

    parser.add_argument(
        "--wire",
        type=int,
        default=None,
        help="Comprimento do fio (opcional, para ambos os algoritmos).",
    )

    return parser.parse_args()


def choose_algorithm() -> str:
    """
    Pergunta ao usuário qual algoritmo deseja executar caso não tenha sido passado via argumentos.

    Args:
        None

    Returns:
        str: Algoritmo escolhido ('greedy' ou 'a_star').
    """
    print("Escolha o algoritmo:")
    print("1) Greedy (Busca Gulosa)")
    print("2) A*")

    choice = input().strip()

    if choice == "1":
        return "greedy"
    elif choice == "2":
        return "a_star"
    else:
        print("Opção inválida.")
        sys.exit(1)


def ask_wire_limit() -> int | None:
    """
    Pergunta ao usuário se deseja adicionar um limite de fio e retorna o valor.

    Args:
        None

    Returns:
        int | None: Comprimento do fio definido pelo usuário ou None se não desejar adicionar.
    """
    print("Deseja adicionar um limite de fio? (s/n)")

    resp = input().strip().lower()
    
    if resp == "s":
        try:
            print("Qual o comprimento do fio?")

            return int(input().strip())
        except ValueError:
            print("Valor inválido para comprimento do fio.")

            sys.exit(1)

    return None


def execute_algorithm(
    alg: str,
    start: str,
    goal: str,
    graph: Graph,
    h_map: HeapMap,
    wire_limit: int | None,
) -> MazeSearchResult:
    """
    Executa o algoritmo selecionado com os parâmetros fornecidos.

    Args:
        alg (str): Algoritmo a ser executado ('greedy' ou 'a_star').
        start (str): Nó inicial da busca.
        goal (str): Nó objetivo da busca.
        graph (Graph): Grafo representado como lista de adjacência.
        h_map (HeapMap): Dicionário de heurísticas para cada nó.
        wire_limit (int | None): Limite opcional do comprimento do fio.

    Returns:
        MazeSearchResult: Resultado da busca contendo:
            - path (list[str] | None): Caminho encontrado ou None se não houver.
            - distance (float): Custo do caminho ou float('inf') se não houver.
            - expanded (int): Número de nós expandidos durante a busca.
    """
    if alg == "greedy":
        return greedy_search_start(start, goal, graph, h_map, wire_limit=wire_limit)
    elif alg == "a_star":
        return a_search_start(start, goal, graph, h_map, wire_limit=wire_limit)
    else:
        print("Algoritmo não reconhecido.")
        sys.exit(1)


def print_result(result: MazeSearchResult):
    """
    Exibe o caminho, distância e medida de desempenho.

    Args:
        result (MazeSearchResult): Resultado da busca.

    Returns:
        None
    """
    path = result["path"]
    dist = result["distance"]
    expanded = result["expanded"]

    if path is None:
        print("Distância: inf")
        print("Caminho: inexistente")
    else:
        print(f"Distância: {dist}")
        print("Caminho: " + " – ".join(path))
        
    print(f"Medida de desempenho: {expanded}\n")


def start_maze_search():
    """
    Função principal que orquestra a execução da busca no labirinto.

    Passos:
        1. Processa argumentos da linha de comando.
        2. Carrega o grafo e heurísticas a partir do arquivo.
        3. Pergunta ao usuário sobre algoritmo e wire limit se necessário.
        4. Executa o algoritmo selecionado.
        5. Exibe o resultado da busca.

    Args:
        None

    Returns:
        None
    """
    try:
        args = parse_args()
        start, goal, directed, graph, h_map = parse_graph_from_file(args.file)

        alg = args.alg or choose_algorithm()
        wire_limit = args.wire or ask_wire_limit()

        result = execute_algorithm(alg, start, goal, graph, h_map, wire_limit)

        print_result(result)

    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)

        sys.exit(1)


if __name__ == "__main__":
    start_maze_search()
