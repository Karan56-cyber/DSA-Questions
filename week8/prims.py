import heapq

def prim(graph,start):

    visited=set()

    heap=[(0,start)]

    total=0

    while heap:

        weight,node=heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)

        total+=weight

        for neighbor,w in graph[node]:

            if neighbor not in visited:
                heapq.heappush(heap,(w,neighbor))

    return total


def main():

    graph={
        0:[(1,2),(3,6)],
        1:[(0,2),(2,3),(3,8)],
        2:[(1,3),(3,7)],
        3:[(0,6),(1,8),(2,7)]
    }

    print(prim(graph,0))


if __name__=="__main__":
    main()