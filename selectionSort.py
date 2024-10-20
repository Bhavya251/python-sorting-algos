def selectionSort(unsortedArr):

    for i in range(len(unsortedArr) - 1):
        minEle = i

        for j in range(i + 1, len(unsortedArr)):
            if unsortedArr[j] < unsortedArr[minEle]:
                minEle = j

        unsortedArr[i], unsortedArr[minEle] = unsortedArr[minEle], unsortedArr[i]
        print(unsortedArr)

    return unsortedArr


if __name__ == '__main__':
    arr = [10, 7, 4, 2, 8, 5, 3, 9, 1, 6]
    print("Unsorted Array: " + str(arr))
    selectionSort(arr)
    print("Sorted Array: " + str(arr))
