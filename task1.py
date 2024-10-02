import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
]
routes = [
    ('C', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'G'), ('F', 'H'), ('G', 'H'), ('A','H')
]

G.add_nodes_from(stations)
G.add_edges_from(routes)

colors = ['lightblue', 'orange', 'lightgreen', 'red', 'purple', 'yellow', 'pink', 'gray']
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color=colors, node_size=2000, edge_color='gray', font_size=15)
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")

degrees = dict(G.degree())
print("Ступінь кожної вершини:")
for station, degree in degrees.items():
    print(f"{station}: {degree}")