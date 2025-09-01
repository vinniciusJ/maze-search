from typing import Optional

from utils.view import format_frontier
from utils.graph import reconstruct_path
from schemas.graph import MazeSearchResult, Graph


def dfs_start(
    start: str,
    goal: str,
    graph: Graph,
    wire_limit: Optional[int] = None,
) -> MazeSearchResult:
    """Executa a busca em profundidade (DFS) para encontrar um caminho em um grafo.

    Este algoritmo explora o mais fundo possível ao longo de cada ramo antes
    de retroceder (backtracking). Ele não garante encontrar o caminho mais curto
    (não é ótimo), mas é eficiente em termos de memória em comparação com a
    busca em largura. A função também suporta um limite de custo opcional para
    descartar caminhos que excedam um determinado valor.

    Args:
        start (str): O nó inicial da busca.
        goal (str): O nó objetivo a ser alcançado.
        graph (Graph): Um dicionário representando o grafo como uma lista de
            adjacência. As chaves são os nós e os valores são listas de
            tuplas, onde cada tupla contém um nó vizinho e o custo para
            alcançá-lo.
        wire_limit (Optional[int]): O custo máximo permitido para um caminho.
            Caminhos que excederem este limite serão ignorados. Se None,
            nenhum limite é aplicado. O padrão é None.

    Returns:
        MazeSearchResult: Um objeto contendo o resultado da busca, incluindo:
            - `path` (list[str] | None): Uma lista de nós representando o
              caminho do início ao fim, ou None se nenhum caminho for encontrado.
            - `distance` (float): O custo total do caminho encontrado, ou
              infinito se nenhum caminho for encontrado.
            - `expanded` (int): O número total de nós expandidos durante a busca.
    """
    print("Início da execução")

    stack = [start]

    g = {start: 0}
    came_from = {}
    visited = set()
    expanded = 0
    iteration = 0

    while stack:
        iteration += 1

        snapshot = []
        for node in reversed(stack):
            gn = g.get(node, 0)
            hn = 0
            fn = gn + hn

            snapshot.append((node, gn, hn, fn))

        print(f"Iteração {iteration}:")
        print("Lista:", format_frontier(snapshot))
        print(f"Medida de desempenho: {expanded}")

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        expanded += 1

        if current == goal:
            path = reconstruct_path(came_from, current)

            print("Fim da execução")

            return MazeSearchResult(path=path, distance=g[current], expanded=expanded)

        for neighbor, cost in reversed(graph.get(current, [])):
            if neighbor in visited:
                continue

            tentative_g = g[current] + cost

            if wire_limit is not None and tentative_g > wire_limit:
                continue

            g[neighbor] = tentative_g
            came_from[neighbor] = current
            stack.append(neighbor)

    print("Fim da execução")

    return MazeSearchResult(path=None, distance=float("inf"), expanded=expanded)
