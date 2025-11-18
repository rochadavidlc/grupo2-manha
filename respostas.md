navigate_three
resposta: 
Ao executar o software e utilizar uma opção de "sim" ou "nao" o arquivo dá um erro com a mensagem "Implemente a função "navigate_tree."
Ao implementar essa função com a orientação do tree_logic.py este problema se resolve. 

"""
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas (lista de strings).
    Cada resposta deve ser 'sim' ou 'não' (aceite 'nao' como 'não').
    Retorna a decisão final (string) quando alcançar uma folha.
    Se a sequência terminar antes de chegar a uma folha, levante ValueError com dica.
    Se alguma resposta for inválida, levante ValueError com mensagem clara.
    >>> # Exemplo (não-executável aqui): navigate_tree(root, ["sim", "não"]) -> "É um pardal/pássaro diurno"
    """

    def navigate_tree(node, answers):
    while node is not None and not is_leaf(node):      
            if not answers:
                raise ValueError("Faltam respostas para concluir a decisão.")
            
            answer = answers.pop(0).strip().lower()
            if answer == "sim":
                node = node.yes

            elif answer == "não" or answer == "nao":
                node = node.no

            else:
                raise ValueError(f"Resposta inválida: '{answer}'. Responda apenas 'sim' ou 'não'.")
            
        if is_leaf(node):
            return node.question
        else:
            raise ValueError("Faltam respostas para concluir a decisão.")

connected
resposta:
Ao executar o software e utilizar uma opção de conectar duas pessoas A e B, outro erro aparece com a mensagem "Implemente a função connected usando apenas listas."
Ao implementar essa função com a orientação do graph_logic.py este problema se resolve.

"""
Percorre a árvore a partir de 'node' seguindo a sequência de respostas (lista de strings).
Cada resposta deve ser 'sim' ou 'não' (aceite 'nao' como 'não').
Retorna a decisão final (string) quando alcançar uma folha.
Se a sequência terminar antes de chegar a uma folha, levante ValueError com dica.
Se alguma resposta for inválida, levante ValueError com mensagem clara.
>>> # Exemplo (não-executável aqui): navigate_tree(root, ["sim", "não"]) -> "É um pardal/pássaro diurno"
"""

    def connected(graph, a, b):
    def norm(x):
        return x.strip().lower() if isinstance(x, str) else x

    if a is None or b is None:
        return False

    a_n = norm(a)
    b_n = norm(b)

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

    if a_n not in nodes or b_n not in nodes:
        return False

    if a_n == b_n:
        return True

    if b_n in adj.get(a_n, []):
        return True
    if a_n in adj.get(b_n, []):
        return True

    return False
