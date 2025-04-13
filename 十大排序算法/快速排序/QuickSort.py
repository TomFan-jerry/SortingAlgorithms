# 算法步骤：
# 1.从数列中挑出一个元素，称为 “基准”（pivot）。
# 2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。


from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    #每次以数组中间元素为基准数
    pivot = arr[len(arr) // 2]
    #与基准数作比较
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    #考虑到重复的元素，不在left和right数组添加=判断以避免无限循环（如[5, 5, 5]）
    mid = [x for x in arr if x == pivot]

    #递归调用
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(quick_sort(test_array))