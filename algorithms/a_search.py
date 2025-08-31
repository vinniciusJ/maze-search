import heapq

from typing import Optional

from utils.view import format_frontier
from utils.graph import reconstruct_path
from types.graph import Graph, MazeSearchResult, HeapMap


def a_search_start(
    start: str,
    goal: str,
    graph: Graph,
    h_map: HeapMap,
    wire_limit: Optional[int] = None,
) -> MazeSearchResult:
    """
    Executa o algoritmo de busca A* para encontrar o caminho ótimo entre um nó inicial e um nó objetivo em um grafo ponderado.

    Esta implementação utiliza uma fila de prioridade (heap) para explorar os nós com base na soma do custo real
    a partir do nó inicial (`g`) e da estimativa heurística (`h`) até o objetivo.
    Opcionalmente, um limite de fio (wire_limit) pode ser aplicado para restringir o custo máximo do caminho.

    Args:
        start (str): Nó inicial da busca.
        goal (str): Nó objetivo a ser alcançado.
        graph (Graph):
            Grafo representado como lista de adjacência, onde cada chave é um nó e
            o valor é uma lista de tuplas `(vizinho, custo)`.
        h_map (HeapMap):
            Dicionário que mapeia cada nó para o seu valor heurístico (`h`) até o objetivo.
        wire_limit (Optional[int], opcional):
            Custo máximo permitido para o caminho (comprimento do fio). Se `None`, nenhum limite é aplicado.
            Padrão é `None`.

    Returns:
        MazeSearchResult:
            Um dicionário tipado contendo:
            - `path` (list[str] | None): O caminho ótimo do nó inicial até o objetivo ou `None` caso não exista caminho.
            - `distance` (float): O custo total do caminho encontrado, ou `float("inf")` caso não exista caminho.
            - `expanded` (int): Quantidade de nós expandidos durante a busca.
    """
    counter = 0
    heap = []
    g = {start: 0}
    came_from = {}
    expanded = 0
    iteration = 0

    h0 = h_map.get(start, 0)

    heapq.heappush(heap, (h0, counter, start))

    while heap:
        iteration += 1

        tmp = sorted(heap)
        snapshot = []

        for fprio, tie, node in tmp:
            gn = g.get(node, float("inf"))
            hn = h_map.get(node, 0)
            fn = gn + hn

            snapshot.append((node, gn, hn, fn))

        print(f"Iteração {iteration}:")
        print("Lista:", format_frontier(snapshot))
        print(f"Medida de desempenho: {expanded}")

        if wire_limit is not None:
            top_f, _, top_node = tmp[0]
            remaining = wire_limit - g.get(top_node, float("inf"))

            print(f"Fio restante: {max(0, remaining)}")

        f_current, _, current = heapq.heappop(heap)
        expanded += 1

        if current == goal:
            path = reconstruct_path(came_from, current)

            print("Fim da execução")

            return MazeSearchResult(distance=g[current], expanded=expanded, path=path)

        for neighbor, cost in graph.get(current, []):
            new_g = g[current] + cost

            if wire_limit is not None and new_g > wire_limit:
                if wire_limit - g[current] <= 0:
                    print("Fio restante 0 – Caminho descartado")

                continue

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                came_from[neighbor] = current
                counter += 1
                f_neighbor = new_g + h_map.get(neighbor, 0)

                heapq.heappush(heap, (f_neighbor, counter, neighbor))

    print("Fim da execução")

    return MazeSearchResult(distance=float("inf"), expanded=expanded, path=None)
