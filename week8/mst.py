def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent,parent[x])


def union(parent,x,y):
    px=find(parent,x)
    py=find(parent,y)

    if px!=py:
        parent[py]=px
        return True

    return False


def max_spanning(vertices,edges):

    parent=list(range(vertices))

    edges.sort(key=lambda x:x[2],reverse=True)

    total=0

    for u,v,w in edges:

        if union(parent,u,v):
            total+=w

    return total


def main():

    vertices=4

    edges=[
        (0,1,10),
        (0,2,6),
        (0,3,5),
        (1,3,15),
        (2,3,4)
    ]

    print(max_spanning(vertices,edges))


if __name__=="__main__":
    main()