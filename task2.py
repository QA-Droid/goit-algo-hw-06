import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dfs_edges, bfs_edges

G = nx.Graph()

stations = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
]
routes = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'G'), ('F', 'H'), ('G', 'H'),
    ('A', 'I'), ('I', 'J'), ('J', 'F'), ('B', 'F'),
    ('C', 'B'), ('G', 'D'), ('H', 'E')
]

G.add_nodes_from(stations)
G.add_edges_from(routes)

colors = ['lightblue', 'orange', 'lightgreen', 'red', 'purple', 'yellow', 'pink', 'gray', 'green', 'blue']
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color=colors, node_size=2000, edge_color='gray', font_size=15)
plt.show()

dfs_path = list(dfs_edges(G, source='A'))
print("DFS шлях (від 'A'):", dfs_path)
bfs_path = list(bfs_edges(G, source='A'))
print("BFS шлях (від 'A'):", bfs_path)

print("\nПорівняння результатів:")
print(f"DFS обійшов {len(dfs_path)} ребер.")
print(f"BFS обійшов {len(bfs_path)} ребер.")