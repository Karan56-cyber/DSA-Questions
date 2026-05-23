def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))


def main():
    arr1 = [1,2,3,4,5]
    arr2 = [3,4,5,6,7]

    result = common_elements(arr1, arr2)
    print("Common elements:", result)


if __name__ == "__main__":
    main()