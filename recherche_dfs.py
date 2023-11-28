import networkx as nx
from File import *

def chercher_dfs(laby: nx.Graph, source: int = None, destination: int = None) -> list:
    """ Cherche le chemin entre les sommets source et destination
        selon le parcours en profondeur (DFS) avec une file personnalisée.
    """
    # Initialisation des sommets source et destination s'ils ne sont pas renseignés
    # Récupère la liste des sommets
    nodes = list(laby.nodes())
    # Si source n'est pas renseigné, alors on impose source = 0
    if source is None:
        source = nodes[0]
    # Si destination n'est pas renseigné, alors on impose destination = dernier sommet
    if destination is None:
        destination = nodes[-1]

    # Liste pour stocker le chemin
    chemin = []

    # Utilisation de la classe File personnalisée
    file_personnalisee = File()

    # Dictionnaire pour suivre les sommets visités
    visited = {node: False for node in laby.nodes()}
    visited[source] = True

    file_personnalisee.enfiler(source)

    while not file_personnalisee.vide():
        current_node = file_personnalisee.defiler()

        # Ajoute le sommet au chemin
        chemin.append(current_node)

        if current_node == destination:
            # Destination atteinte, retourne le chemin
            return chemin

        # Cherche un voisin non visité
        for neighbor in laby.neighbors(current_node):
            if not visited[neighbor]:
                file_personnalisee.enfiler(neighbor)
                visited[neighbor] = True

    return chemin

if __name__ == "__main__":
    # Création du labyrinthe de test
    aretes = [(0, 1), (0, 4), (1, 0), (1, 5), (2, 6), (3, 7), (4, 0), (4, 5), (5, 1),
              (5, 4), (5, 6), (5, 9), (6, 2), (6, 5), (6, 7), (6, 10), (7, 3), (7, 6),
              (8, 9), (9, 5), (9, 8), (9, 10), (10, 6), (10, 9), (10, 11), (11, 10)]
    colonnes = 4
    lignes = 3
    nb_sommets = colonnes * lignes
    noeuds = list(range(nb_sommets))
    Labyrinthe = nx.Graph()
    Labyrinthe.add_nodes_from(noeuds)
    Labyrinthe.add_edges_from(aretes)

    chemin_dfs = chercher_dfs(Labyrinthe)
    print("Chemin DFS:", chemin_dfs)
