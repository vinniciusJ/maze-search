from typing import Dict, List, Tuple, TypeAlias, TypedDict, Optional

Graph: TypeAlias = Dict[str, List[Tuple[str, int]]]
"""Representa um grafo como lista de adjacência.

Cada chave é um nó representado por uma string.
Cada valor é uma lista de tuplas (vizinho, custo), onde:
    - vizinho (str): Nó adjacente.
    - custo (int): Custo para ir até o nó vizinho.
"""

HeapMap: TypeAlias = Dict[str, int]
"""Representa um mapa heurístico de nós para valores inteiros.

Usado em algoritmos de busca informada (A*, Greedy), onde cada nó tem um valor
estimado (heurística) até o objetivo.

Chaves:
    - str: nome do nó.
Valores:
    - int: valor heurístico associado ao nó.
"""


class MazeSearchResult(TypedDict):
    """Representa o resultado de uma busca em um grafo ou labirinto.

    Atributos:
        path (Optional[List[str]]): Lista de nós que compõem o caminho encontrado do início ao objetivo.
                                     Retorna None se não houver caminho.
        distance (float): Custo total do caminho encontrado. Retorna float("inf") se não houver caminho.
        expanded (int): Número de nós expandidos durante a busca.
    """

    path: Optional[List[str]]
    distance: float
    expanded: int
