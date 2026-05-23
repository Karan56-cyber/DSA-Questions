def bellman_ford(vertices,edges,source):

    distance=[float("inf")]*vertices
    distance[source]=0

    for i in range(vertices-1):

        for u,v,w in edges:

            if distance[u]!=float("inf") and distance[u]+w<distance[v]:
                distance[v]=distance[u]+w

    print(distance)


def main():
    edges=[
        (0,1,-1),
        (0,2,4),
        (1,2,3),
        (1,3,2),
        (1,4,2),
        (4,3,-3)
    ]

    bellman_ford(5,edges,0)


if __name__=="__main__":
    main()