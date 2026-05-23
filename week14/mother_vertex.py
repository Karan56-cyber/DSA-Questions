def dfs(graph,node,visited):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(graph,neighbor,visited)


def mother_vertex(graph):

    visited=set()

    last=0

    for i in graph:

        if i not in visited:
            dfs(graph,i,visited)
            last=i

    visited.clear()

    dfs(graph,last,visited)

    if len(visited)==len(graph):
        return last

    return -1


graph={
0:[1,2],
1:[3],
2:[],
3:[]
}

print(mother_vertex(graph))