# 算法步骤：
# 1.选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
# 2.按增量序列个数 k，对序列进行 k 趟排序；
# 3.每趟排序，根据对应的增量 ti，将待排序列分割成若干个长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。


from typing import List

def shell_sort(arr: List[int]) -> List[int]:
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):#相当于以gap为单位进行插入排序（插入排序是以1为单位，详见InsertionSort）
            current = arr[i]
            pre_index = i - gap
            while pre_index >= 0 and current < arr[pre_index]:
                arr[pre_index + gap] = arr[pre_index]
                pre_index -= gap
            arr[pre_index + gap] = current
        gap //= 2

    return  arr


if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(shell_sort(test_array))