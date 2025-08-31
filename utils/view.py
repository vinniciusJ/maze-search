def format_frontier(entries: list[tuple[str, int, int, int]]) -> str:
    """
    Formata uma lista de nós do frontier (fronteira) de uma busca para exibição legível.

    Cada entrada representa um nó expandido, com os custos g, h e f.

    Args:
        entries (list[tuple[str, int, int, int]]): Lista de tuplas no formato (nó, g, h, f), onde:
            - nó (str): Identificador do nó.
            - g (int): Custo acumulado desde o nó inicial até este nó.
            - h (int): Valor heurístico estimado até o objetivo.
            - f (int): Soma de g + h, usada como prioridade na busca.

    Returns:
        str: Uma string formatada mostrando cada nó na forma "(nó: g + h = f)" separada por espaços,
             na ordem recebida.
    """
    parts = []

    for n, g, h, f in entries:
        parts.append(f"({n}: {g} + {h} = {f})")

    return " ".join(parts)
