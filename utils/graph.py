import re
import sys

from collections import defaultdict


def reconstruct_path(came_from: dict[str, str], current: str) -> list[str]:
    """
    Reconstrói o caminho desde o nó inicial até o nó atual usando o mapa `came_from`.

    Args:
        came_from (dict[str, str]): Dicionário mapeando cada nó para seu predecessor no caminho.
        current (str): Nó final a partir do qual o caminho será reconstruído.

    Returns:
        list[str]: Lista de nós representando o caminho do início até o nó atual.
    """
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    return path


def parse_graph_from_file(
    file_path: str,
) -> tuple[bool, int, int, bool, dict[str, list[tuple[str, int]]], dict[str, int]]:
    """
    Lê um arquivo de definição de grafo e extrai informações sobre o grafo, nós inicial e final,
    direção das arestas e heurísticas.

    O arquivo deve conter definições nos seguintes formatos:
        - ponto_inicial(NÓ).
        - ponto_final(NÓ).
        - orientado(s/n).
        - pode_ir(NÓ1, NÓ2, CUSTO).
        - h(NÓ, OBJETIVO, VALOR).

    Comentários iniciados com `%` são ignorados.

    Args:
        file_path (str): Caminho para o arquivo de definição do grafo.

    Returns:
        tuple[str, str, bool, dict[str, list[tuple[str, int]]], dict[str, int]]:
            Uma tupla contendo:
            - start (str): Nó inicial.
            - goal (str): Nó objetivo.
            - directed (bool): Indica se o grafo é dirigido (`True`) ou não (`False`).
            - graph (dict[str, list[tuple[str, int]]]): Grafo como lista de adjacência.
            - h (dict[str, int]): Dicionário de heurísticas mapeando cada nó para seu valor.

    Raises:
        ValueError: Se o arquivo não contiver `ponto_inicial(...)` ou `ponto_final(...)`.
    """
    start = None
    goal = None
    directed = True
    graph = defaultdict(list)
    h = {}
    specified_goal_for_h = None

    re_comment = re.compile(r"%.*$")
    re_start = re.compile(r"\s*ponto_inicial\(\s*([a-zA-Z0-9_]+)\s*\)\s*\.\s*$")
    re_goal = re.compile(r"\s*ponto_final\(\s*([a-zA-Z0-9_]+)\s*\)\s*\.\s*$")
    re_oriented = re.compile(r"\s*orientado\(\s*([snSN])\s*\)\s*\.\s*$")

    re_edge = re.compile(
        r"\s*pode_ir\(\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s*,\s*([0-9]+)\s*\)\s*\.\s*$"
    )

    re_h = re.compile(
        r"\s*h\(\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s*,\s*([0-9]+)\s*\)\s*\.\s*$"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        for raw in f:
            line = re_comment.sub("", raw).strip()

            if not line:
                continue

            m = re_start.match(line)

            if m:
                start = m.group(1)

                continue

            m = re_goal.match(line)

            if m:
                goal = m.group(1)

                continue

            m = re_oriented.match(line)

            if m:
                directed = m.group(1).lower() == "s"

                continue

            m = re_edge.match(line)

            if m:
                a, b, c = m.group(1), m.group(2), int(m.group(3))

                graph[a].append((b, c))

                if not directed:
                    graph[b].append((a, c))

                graph.setdefault(a, graph[a])
                graph.setdefault(b, graph[b])

                continue

            m = re_h.match(line)

            if m:
                n, g, val = m.group(1), m.group(2), int(m.group(3))
                h[n] = val

                specified_goal_for_h = g

                continue

    if start is None or goal is None:
        raise ValueError("Arquivo deve conter ponto_inicial(...) e ponto_final(...).")

    if specified_goal_for_h and specified_goal_for_h != goal:
        print(
            f"Aviso: heurística h(*,{specified_goal_for_h},*) difere do ponto_final declarado ({goal}). Usando h conforme arquivo.",
            file=sys.stderr,
        )

    graph.setdefault(start, [])
    graph.setdefault(goal, graph.get(goal, []))

    return start, goal, directed, graph, h
