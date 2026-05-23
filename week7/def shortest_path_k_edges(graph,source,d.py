def shortest_path_k_edges(graph,source,destination,k):

    n=len(graph)

    dp=[[float("inf")]*n for _ in range(k+1)]

    dp[0][source]=0

    for e in range(1,k+1):
        for u in range(n):
            for v,w in graph[u]:
                if dp[e-1][u] != float("inf"):
                    dp[e][v]=min(dp[e][v],dp[e-1][u]+w)

    return dp[k][destination]


def main():

    graph={
        0:[(1,10),(2,3)],
        1:[(3,2)],
        2:[(1,1),(3,8)],
        3:[]
    }

    print(shortest_path_k_edges(graph,0,3,2))


if __name__=="__main__":
    main()