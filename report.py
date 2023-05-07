import matplotlib.pyplot as plt
import networkx as nx
import requests
from bs4 import BeautifulSoup
from matplotlib import pylab

G = nx.read_adjlist("googleschoolar.txt", create_using=nx.Graph)

# Calculate the cluster coefficient, distribution of degrees, and average path length
cc = nx.average_clustering(G)
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = nx.degree_histogram(G)
avg_path_length = nx.average_shortest_path_length(G)

# Print the results
print(f"Cluster coefficient: {cc}")
print(f"Degree distribution: {degree_count}")
print(f"Average path length: {avg_path_length}")
# plt.hist(degree_count,4000)
# plt.show()
