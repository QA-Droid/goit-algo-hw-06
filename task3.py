import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
]
routes_with_weights = [
    ('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 1), ('C', 'D', 1.5),
    ('D', 'E', 2), ('E', 'F', 1), ('F', 'G', 1.5), ('F', 'H', 2),
    ('G', 'H', 1), ('A', 'I', 3), ('I', 'J', 1), ('J', 'F', 2.5),
    ('B', 'F', 2), ('C', 'B', 1), ('G', 'D', 2), ('H', 'E', 2.5)
]

G.add_nodes_from(stations)
G.add_weighted_edges_from(routes_with_weights)

pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G, 'weight')
colors = ['lightblue', 'orange', 'lightgreen', 'red', 'purple', 'yellow', 'pink', 'gray', 'green', 'blue']
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, edge_color='gray', font_size=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
plt.show()

shortest_paths = nx.single_source_dijkstra_path_length(G, source='A')
print("Найкоротші шляхи від вузла 'A' до всіх інших вершин:")
for target, length in shortest_paths.items():
    print(f"Від 'A' до '{target}' = {length} одиниць")

all_shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G))
print("\nНайкоротші шляхи між усіма вершинами:")
for source, paths in all_shortest_paths.items():
    print(f"\nВершина '{source}':")
    for target, length in paths.items():
        print(f"  до '{target}' = {length} одиниць")