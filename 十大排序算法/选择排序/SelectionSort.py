# 算法步骤：
# 1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
# 2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 3.重复第二步，直到所有元素均排序完毕。
from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(selection_sort(nums))