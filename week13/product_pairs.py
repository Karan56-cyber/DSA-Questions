def product_pairs(arr,target):

    seen=set()

    for num in arr:

        if num!=0 and target%num==0:

            x=target//num

            if x in seen:
                print(x,num)

        seen.add(num)


arr=[2,4,5,10,20]
target=20

product_pairs(arr,target)