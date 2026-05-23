def knapsack(weight,value,capacity):

    n=len(value)

    dp=[[0]*(capacity+1) for i in range(n+1)]

    for i in range(1,n+1):

        for w in range(capacity+1):

            if weight[i-1]<=w:

                dp[i][w]=max(
                    value[i-1]+dp[i-1][w-weight[i-1]],
                    dp[i-1][w]
                )

            else:
                dp[i][w]=dp[i-1][w]

    return dp[n][capacity]


weight=[10,20,30]
value=[60,100,120]
capacity=50

print(knapsack(weight,value,capacity))