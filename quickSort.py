def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(unsortedArr, low, high):
    if low < high:
        pi = partition(unsortedArr, low, high)
        quickSort(unsortedArr, low, pi - 1)
        quickSort(unsortedArr, pi, high)

    return unsortedArr


if __name__ == '__main__':
    arr = [10, 7, 4, 2, 8, 5, 3, 9, 1, 6]
    print("Unsorted Array: " + str(arr))
    quickSort(arr, 0, len(arr) - 1)
    print("Sorted Array: " + str(arr))
