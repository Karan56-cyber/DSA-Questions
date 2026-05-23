def two_sum(arr,target):
    seen={}

    for num in arr:
        x=target-num

        if x in seen:
            return [x,num]

        seen[num]=True

    return []


def main():
    arr=[2,7,11,15]
    target=9

    print("Pair:",two_sum(arr,target))


if __name__=="__main__":
    main()