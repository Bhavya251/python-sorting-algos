def insertionSort(unsortedArr):
    for i in range(1, len(unsortedArr)):
        key = unsortedArr[i]
        j = i - 1
        while j >= 0 and key < unsortedArr[j]:
            unsortedArr[j + 1] = unsortedArr[j]
            j -= 1

        unsortedArr[j + 1] = key
        print(unsortedArr)
    return unsortedArr


if __name__ == '__main__':
    arr = [10, 7, 4, 2, 8, 5, 3, 9, 1, 6]
    print("Unsorted Array: " + str(arr))
    insertionSort(arr)
    print("Sorted Array: " + str(arr))
