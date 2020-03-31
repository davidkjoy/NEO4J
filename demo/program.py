from py2neo import Graph
graph = Graph("bolt://myserver:7687", auth=("neo4j", "graph"))

data = graph.run("MATCH(n) RETURN n").to_table()
print(type(data))
