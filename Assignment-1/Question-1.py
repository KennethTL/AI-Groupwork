import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
nodes=["Sports Complex", "Siwaka","Ph 1.A", "Phase 2", "J1", "Mada", "STC", "Phase 3", "Parking Lot","Ph 1.B"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes

G.add_edge("Sports Complex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph 1.A",weight="10")
G.add_edge("Siwaka","Ph 1.B",weight="230")
G.add_edge("Ph 1.B","STC",weight="50")
G.add_edge("Ph 1.A", "Ph 1.B",weight="100")
G.add_edge("Ph 1.A","Mada",weight="850")
G.add_edge("Ph 1.B","Phase 2",weight="112")
G.add_edge("STC","Phase 2",weight="50")
G.add_edge("STC","Parking Lot",weight="250")
G.add_edge("Phase 2","Phase 3",weight="500")
G.add_edge("Phase 3","Parking Lot",weight="350")
G.add_edge("Phase 2","J1",weight="600")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Mada","Parking Lot",weight="450")

G.nodes["Sports Complex"]['pos']=(0,0)
G.nodes["Siwaka"]['pos']=(6,0)
G.nodes["Ph 1.A"]['pos']=(10,0)
G.nodes["Phase 2"]['pos']=(15,-3)
G.nodes["J1"]['pos']=(18,-3)
G.nodes["Mada"]['pos']=(24,-3)
G.nodes["STC"]['pos']=(10,-6)
G.nodes["Phase 3"]['pos']=(18,-6)
G.nodes["Parking Lot"]['pos']=(18,-9)
G.nodes["Ph 1.B"]['pos']=(10,-3)



node_pos = nx.get_node_attributes(G,'pos')
arc_weight=nx.get_edge_attributes(G,'weight')
#print (nx.info(G))


nx.draw_networkx(G, node_pos, node_size=800)
nx.draw_networkx_edges(G, node_pos,width=2)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)

#nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
#nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)

plt.axis('off')
plt.show()













