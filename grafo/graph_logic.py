
# graph_logic.py — você edita APENAS este arquivo nesta atividade.
# Dica: use apenas LISTAS para a fila/estrutura de dados (nada de deque).
# Você pode fazer BFS com:
#   fila = [a]; visitados = [a]
#   while fila:
#       u = fila.pop(0)          # remove o primeiro
#       if u == b: return True
#       for v in graph.get(u, []):
#           if v not in visitados:
#               visitados.append(v)
#               fila.append(v)
#   return False
#
# Alternativamente, pode usar DFS com uma lista como "pilha":
#   pilha = [a]; visitados = []
#   while pilha:
#       u = pilha.pop()          # remove o último
#       ...
#   return False

def connected(graph, a, b):
    """
    Retorna True apenas se 'a' e 'b' estiverem diretamente ligados:
    - b aparece na lista de adjacência de a, ou
    - a aparece na lista de adjacência de b
    Normaliza nomes (case-insensitive, strip).
    """
    # função auxiliar para normalizar nomes
    def norm(x):
        return x.strip().lower() if isinstance(x, str) else x

    if a is None or b is None:
        return False

    a_n = norm(a)
    b_n = norm(b)

    # coletar nós mencionados e construir adjacência normalizada apenas com relações diretas (chave -> valor, valor -> chave)
    nodes = set()
    adj = {}
    for u, neigh in graph.items():
        u_n = norm(u)
        nodes.add(u_n)
        adj.setdefault(u_n, [])
        for v in neigh:
            v_n = norm(v)
            nodes.add(v_n)
            adj[u_n].append(v_n)

    # se A ou B não aparecem no grafo, não estão conectados
    if a_n not in nodes or b_n not in nodes:
        return False

    # mesmo nó -> considerar conectado
    if a_n == b_n:
        return True

    # verificação de ligação direta (ambas as direções)
    if b_n in adj.get(a_n, []):
        return True
    if a_n in adj.get(b_n, []):
        return True

    return False
