from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(nums))
