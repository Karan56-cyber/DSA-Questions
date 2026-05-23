def duplicate_window(arr,k):

    window=set()

    for i in range(len(arr)):

        if arr[i] in window:
            return True

        window.add(arr[i])

        if len(window)>k:
            window.remove(arr[i-k])

    return False


arr=[1,2,3,1,4,5]
k=3

print(duplicate_window(arr,k))