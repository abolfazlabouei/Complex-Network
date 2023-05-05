import requests
from bs4 import BeautifulSoup
import networkx as nx

# Get the webpage and parse it with BeautifulSoup
url = 'https://www.digikala.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Create a list of all links on the page
urls = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.startswith('https://www.digikala.com/'):
        urls.append(href)

# Create a directed graph and add all links as nodes
G = nx.DiGraph()
for url in urls:
    G.add_node(url)

# Add edges to the graph by crawling the links on the page
for url in urls:
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('https://www.digikala.com/'):
            if href != url:
                G.add_edge(url, href)

# Calculate the cluster coefficient, distribution of degrees, and average path length
cc = nx.average_clustering(G)
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = nx.degree_histogram(G)
avg_path_length = nx.average_shortest_path_length(G)

# Print the results
print(f"Cluster coefficient: {cc}")
print(f"Degree distribution: {degree_count}")
print(f"Average path length: {avg_path_length}")
