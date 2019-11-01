import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [('A','F'),('A','B'),('A','D'),('A','E'),('B','C'),('C','E'),('D','A'),('D','C'),('D','E'),('E','B'),('E','C'),('F','D')]

for edge in edges:
	G.add_edge(edge[0],edge[1])

#可视化
layout = nx.spring_layout(G)
nx.draw(G, pos=layout, with_labels=True, hold=False)
plt.show()

pr = nx.pagerank(G,alpha=0.8,max_iter=100)

print('模型PR值：',pr)
