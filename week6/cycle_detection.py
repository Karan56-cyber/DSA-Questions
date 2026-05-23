def dfs(node,graph,visited,rec_stack):

    visited[node]=True
    rec_stack[node]=True

    for neighbor in graph[node]:

        if not visited[neighbor]:
            if dfs(neighbor,graph,visited,rec_stack):
                return True

        elif rec_stack[neighbor]:
            return True

    rec_stack[node]=False
    return False


def has_cycle(graph):

    n=len(graph)

    visited=[False]*n
    rec_stack=[False]*n

    for i in range(n):
        if not visited[i]:
            if dfs(i,graph,visited,rec_stack):
                return True

    return False


def main():
    graph=[
        [1],
        [2],
        [0]
    ]

    print(has_cycle(graph))


if __name__=="__main__":
    main()