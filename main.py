import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()
G.add_nodes_from(["B", "S1", "S2", "M1", "X1", "X2", "O1", "O2", "M2"])
G.add_edges_from([
    ("B", "S1"), ("B", "S2"), ("B", "M2"), ("B", "O1"),
    ("M2", "O2"), ("S2", "M1"), ("S2", "X1"), ("M1", "X2"), ("X1", "X2")
])

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

# Ступені вершин
print("Ступінь кожної вершини:")
for node in G.nodes:
    print(f"{node}: {G.degree(node)}")

avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
print("Середній ступінь графа:", avg_degree)
# BFS (пошук у ширину)
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(neighbor for neighbor in graph.neighbors(node) if neighbor not in visited)
    
    return traversal_order

# DFS (пошук у глибину)
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            stack.extend(neighbor for neighbor in graph.neighbors(node) if neighbor not in visited)
    
    return traversal_order

# Алгоритм Дейкстри
def dijkstra(graph, start_node):
    import heapq
    
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = 1  # У всіх ребер вага 1, якщо не задано інше
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


start = "B"
print("BFS:", bfs(G, start))
print("DFS:", dfs(G, start))
print("Dijkstra's Shortest Path Distances:", dijkstra(G, start))

bfs_path = bfs(G, start)
dfs_path = dfs(G, start)

print("Порівняння DFS та BFS:")
print("BFS відвідує вершини в ширину, тому спочатку обробляє всі суміжні вершини поточного вузла.")
print("DFS занурюється в глибину, тобто спочатку досліджує один шлях якомога далі.")
print("Отже, порядок обходу різний, оскільки алгоритми мають різну стратегію пошуку.")
print("BFS:", bfs_path)
print("DFS:", dfs_path)

nx.draw(G, with_labels=True)
plt.show()