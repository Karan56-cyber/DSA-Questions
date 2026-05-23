import heapq

def merge(files):

    heapq.heapify(files)

    cost=0

    while len(files)>1:

        a=heapq.heappop(files)
        b=heapq.heappop(files)

        total=a+b

        cost+=total

        heapq.heappush(files,total)

    return cost


def main():

    files=[20,30,10,5]

    print(merge(files))


if __name__=="__main__":
    main()