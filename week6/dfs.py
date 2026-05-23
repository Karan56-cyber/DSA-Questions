def dfs(graph,node,target,visited):

    if node==target:
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph,neighbor,target,visited):
                return True

    return False


def main():
    graph={
        0:[1,2],
        1:[3],
        2:[4],
        3:[],
        4:[]
    }

    print(dfs(graph,0,4,set()))


if __name__=="__main__":
    main()