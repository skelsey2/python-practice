#DFS - Depth First Search/Traversal
# https://favtutor.com/blogs/depth-first-search-python

def dfs(visted, graph, node):
    if node not in visted:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
            

visited = set() # set to keep the visted nodes of graph.
graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

#driver
print("The following is the Depth-First Search")
dfs(visited, graph, '5')
