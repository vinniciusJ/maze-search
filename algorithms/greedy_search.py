import heapq

from typing import Optional

from utils.view import format_frontier
from utils.graph import reconstruct_path
from schemas.graph import MazeSearchResult, HeapMap, Graph


def greedy_search_start(
    start: str,
    goal: str,
    graph: Graph,
    h_map: HeapMap,
    wire_limit: Optional[int] = None,
) -> MazeSearchResult:
    """
    Executa o algoritmo de busca gulosa (Greedy Best-First Search) para encontrar um caminho entre
    um nó inicial e um nó objetivo em um grafo ponderado, com limite opcional de custo do caminho.

    A busca gulosa prioriza os nós com menor valor heurístico (`h`), ignorando o custo acumulado
    desde o início. Este método não garante encontrar o caminho ótimo, mas tende a ser rápido.
    Caso `wire_limit` seja fornecido, caminhos que excedam esse limite são descartados.

    Args:
        start (str): Nó inicial da busca.
        goal (str): Nó objetivo a ser alcançado.
        graph (Graph):
            Grafo representado como lista de adjacência, onde cada chave é um nó e
            o valor é uma lista de tuplas `(vizinho, custo)`.
        h_map (HeapMap):
            Dicionário que mapeia cada nó para seu valor heurístico (`h`) até o objetivo.
        wire_limit (float | None, opcional):
            Custo máximo permitido para o caminho. Caminhos que excederem este limite são ignorados.
            Se `None`, nenhum limite é aplicado. Padrão é `None`.

    Returns:
        MazeSearchResult:
            Um objeto tipado contendo:
            - `path` (list[str] | None): O caminho encontrado do nó inicial até o objetivo ou `None` caso não exista caminho.
            - `distance` (float): O custo total do caminho encontrado, ou `float("inf")` caso não exista caminho.
            - `expanded` (int): Quantidade de nós expandidos durante a busca.
    """
    print("Início da execução")

    counter = 0
    heap = []
    g = {start: 0}
    came_from = {}
    visited = set()
    expanded = 0

    h0 = h_map.get(start, 0)
    heapq.heappush(heap, (h0, counter, start))

    iteration = 0

    while heap:
        iteration += 1

        snapshot = []

        for prio, tie, node in sorted(heap):
            gn = g.get(node, float("inf"))
            hn = h_map.get(node, 0)
            fn = gn + hn
            snapshot.append((node, gn, hn, fn))

        print(f"Iteração {iteration}:")
        print("Lista:", format_frontier(snapshot))
        print(f"Medida de desempenho: {expanded}")

        _, _, current = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)
        expanded += 1

        if current == goal:
            path = reconstruct_path(came_from, current)

            print("Fim da execução")

            return MazeSearchResult(path=path, distance=g[current], expanded=expanded)

        for neighbor, cost in graph.get(current, []):
            tentative_g = g[current] + cost

            if wire_limit is not None and tentative_g > wire_limit:
                continue

            if neighbor not in g or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                came_from[neighbor] = current
                counter += 1
                heapq.heappush(heap, (h_map.get(neighbor, 0), counter, neighbor))

    print("Fim da execução")

    return MazeSearchResult(path=None, distance=float("inf"), expanded=expanded)
