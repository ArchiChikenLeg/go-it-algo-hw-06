import networkx as nx

G = nx.Graph()
G.add_nodes_from(["B", "S1", "S2", "M1", "X1", "X2", "O1", "O2", "M2"])
G.add_edges_from([("B", "S1"),("B", "S2"), ("B","M2"), ("B", "O2"), ("M2", "O2"), ("S2", "M1"), ("S2", "X1"), ("M1", "X1"), ("X1", "X2")])