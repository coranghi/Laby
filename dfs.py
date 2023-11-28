import networkx as nx
from Pile import *

def parcours_dfs(laby: nx.Graph, source: int = None) -> list:
    """ Parcours en profondeur (DFS) avec une pile personnalisée.
    """
    # Initialisation du sommet source s'il n'est pas renseigné
    # Récupère la liste des sommets
    nodes = list(laby.nodes())
    # Si source n'est pas renseigné, alors on impose source = 0
    if source is None:
        source = nodes[0]

    # Liste pour stocker le parcours DFS
    parcours = []

    # Utilisation de la classe Pile personnalisée
    pile_personnalisee = Pile()

    # Dictionnaire pour suivre les sommets visités
    visited = {node: False for node in laby.nodes()}
    visited[source] = True

    pile_personnalisee.empiler(source)

    while not pile_personnalisee.vide():
        current_node = pile_personnalisee.depiler()

        # Ajoute le sommet au parcours
        parcours.append(current_node)

        # Cherche les voisins non visités
        for neighbor in laby.neighbors(current_node):
            if not visited[neighbor]:
                pile_personnalisee.empiler(neighbor)
                visited[neighbor] = True

    return parcours

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

    parcours_dfs_resultat = parcours_dfs(Labyrinthe)
    print("Parcours DFS:", parcours_dfs_resultat)
