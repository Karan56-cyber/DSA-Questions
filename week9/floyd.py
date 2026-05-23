def floyd(graph):

    n=len(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):

                graph[i][j]=min(
                    graph[i][j],
                    graph[i][k]+graph[k][j]
                )

    return graph


def main():

    inf=float("inf")

    graph=[
        [0,5,inf,10],
        [inf,0,3,inf],
        [inf,inf,0,1],
        [inf,inf,inf,0]
    ]

    result=floyd(graph)

    for row in result:
        print(row)


if __name__=="__main__":
    main()