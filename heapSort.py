def heapify(arr, n, i):
    largest = i

    left = 2* i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(unsortedArr):
    n = len(unsortedArr)

    for i in range(n//2 - 1, -1, -1):
        heapify(unsortedArr, n, i)

    for i in range(n - 1, 0, -1):
        unsortedArr[0], unsortedArr[i] = unsortedArr[i], unsortedArr[0]

        heapify(unsortedArr, i, 0)

    return unsortedArr


if __name__ == "__main__":
    arr = [10, 7, 4, 2, 8, 5, 3, 9, 1, 6]
    print("Unsorted Array: " + str(arr))
    heapSort(arr)
    print("Sorted Array: " + str(arr))

