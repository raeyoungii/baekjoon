def selection_sort(arr):
    print(0, arr)
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(i + 1, arr)


def bubble_sort(arr):
    print(0, arr)
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(len(arr) - i, arr)
        if not swapped:
            break


def insertion_sort(arr):
    print(0, arr)
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        print(end, arr)


if __name__ == "__main__":
    A = [7, 2, 8, 4, 3, 1, 3, 5]
    T = int(input())
    if T == 1:
        selection_sort(A)
    elif T == 2:
        bubble_sort(A)
    elif T == 3:
        insertion_sort(A)
