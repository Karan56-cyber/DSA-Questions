import heapq

def dijkstra(graph,source):

    n=len(graph)

    distance=[float("inf")]*n

    distance[source]=0

    pq=[(0,source)]

    while pq:

        dist,node=heapq.heappop(pq)

        for neighbor,weight in graph[node]:

            new_dist=dist+weight

            if new_dist<distance[neighbor]:
                distance[neighbor]=new_dist
                heapq.heappush(pq,(new_dist,neighbor))

    return distance


def main():

    graph={
        0:[(1,4),(2,1)],
        1:[(3,1)],
        2:[(1,2),(3,5)],
        3:[]
    }

    print(dijkstra(graph,0))


if __name__=="__main__":
    main()