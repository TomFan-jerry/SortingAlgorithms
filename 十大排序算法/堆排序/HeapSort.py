# 算法步骤：
# 1.创建一个堆 H[0……n-1]。
# 2.把堆首（最大值）和堆尾互换。
# 3.把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置。
# 4.重复步骤 2，直到堆的尺寸为 1。


from typing import List

def heap_sort(arr: List[int]) -> List[int]:

    #内部方法：调整子树为最大堆（n为当前堆的有效长度，i为需要调整的节点索引）
    def heapify(n: int, i: int) -> None:
        # 假设当前节点i是最大值的位置
        largest = i
        # 左子节点索引
        left = 2 * i + 1
        # 右子节点索引
        right = 2 * i + 2

        # 确定当前节点、左子节点、右子节点中的最大值
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        #最大值不在当前节点，交换并递归调整
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n ,largest)

    # 构建初始最大堆
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(len(arr), i)

    # 逐步提取堆顶最大值并调整堆
    for i in range(len(arr) - 1, 0, -1):
        # 交换堆顶与当前末尾
        arr[i], arr[0] = arr[0], arr[i]
        # 调整剩余元素为最大堆
        heapify(i, 0)

    return arr


if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(heap_sort(test_array))