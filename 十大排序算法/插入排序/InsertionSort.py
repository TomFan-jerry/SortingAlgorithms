# 算法步骤：
# 1.将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
# 2.从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）


from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and current < arr[pre_index]:#比current大的元素全部后移一位
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current#在空位插入current

    return arr

if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(insertion_sort(test_array))