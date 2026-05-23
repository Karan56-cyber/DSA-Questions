def majority(arr):

    arr.sort()

    candidate = arr[len(arr)//2]

    count = arr.count(candidate)

    if count > len(arr)//2:
        return candidate

    return "No Majority"


arr=[2,2,1,2,3,2,2]

print(majority(arr))