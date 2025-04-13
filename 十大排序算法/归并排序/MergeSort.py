# 算法步骤：
# 1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列。
# 2.设定两个指针，最初位置分别为两个已经排序序列的起始位置。
# 3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一个位置。
# 4.重复步骤 3 直到某一个指针达到序列尾。
# 5.将另一序个列剩下的所有元素直接复制到合并序列尾。


from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[: mid], arr[mid:]

        #递归调用，进行数组的切片操作
        merge_sort(left)
        merge_sort(right)

        #比较左右两个切片列表，依次选出最小元素放在开头，若有一个切片列表被选完则直接处理另一个切片列表剩余值
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #处理剩余值，直接按原顺序放入原列表
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(merge_sort(test_array))