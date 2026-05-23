def knapsack(capacity,items):

    items.sort(
        key=lambda x:x[1]/x[0],
        reverse=True
    )

    profit=0

    for weight,value in items:

        if capacity>=weight:
            profit+=value
            capacity-=weight

        else:
            profit+=value*(capacity/weight)
            break

    return profit


def main():

    items=[
        (10,60),
        (20,100),
        (30,120)
    ]

    capacity=50

    print(knapsack(capacity,items))


if __name__=="__main__":
    main()