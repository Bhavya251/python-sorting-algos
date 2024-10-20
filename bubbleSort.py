def bubbleSort(unsortedArr):
    length = len(unsortedArr)

    for i in range(length):

        for j in range(0, length - 1):
            if unsortedArr[j] > unsortedArr[j + 1]:
                temp = unsortedArr[j+1]
                unsortedArr[j+1] = unsortedArr[j]
                unsortedArr[j] = temp
            print(unsortedArr)
    return unsortedArr


if __name__ == '__main__':
    arr = [10, 7, 1, 4, 2, 8, 5, 3, 9, 6]
    print("Unsorted Array: " + str(arr))
    bubbleSort(arr)
    print("Sorted Array: " + str(arr))
