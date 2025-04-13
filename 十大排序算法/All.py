from typing import List

# 1.冒泡排序(BubbleSort)
def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 2.选择排序(SelectionSort)
def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 3.插入排序(InsertionSort)
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        # 比current大的元素全部后移一位
        while pre_index >= 0 and current < arr[pre_index]:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        # 在空位插入current
        arr[pre_index + 1] = current

    return arr


# 4.希尔排序(ShellSort)
def shell_sort(arr: List[int]) -> List[int]:
    gap = len(arr) // 2
    while gap > 0:
        # 相当于以gap为单位进行插入排序（插入排序是以1为单位，详见InsertionSort）
        for i in range(gap, len(arr)):
            current = arr[i]
            pre_index = i - gap
            while pre_index >= 0 and current < arr[pre_index]:
                arr[pre_index + gap] = arr[pre_index]
                pre_index -= gap
            arr[pre_index + gap] = current
        gap //= 2

    return  arr


# 5.归并排序(MergeSort)
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


# 6.快速排序(QuickSort)
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


# 7.堆排序(HeapSort)
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


# 8.计数排序(CountingSort)
def counting_sort(arr: List[int]) -> List[int]:
    # 计算元素实际范围
    max_value = max(arr)
    min_value = min(arr)
    count_length = max_value - min_value + 1

    # 初始化计数数组（长度由元素范围决定，而非最大值）
    count = [0] * count_length

    # 统计元素频率（通过偏移量映射到计数数组索引）
    for a in arr:
        count[a - min_value] += 1

    # 根据计数数组重构排序后的原数组
    i = 0
    for index in range(count_length):
        #还原初始数值
        value = min_value + index
        for n in range(count[index]):
            arr[i] = value
            i += 1

    return arr


# 9.桶排序
def bucket_sort(arr: List[int]) -> List[int]:
    # 内部插入排序函数（对每个桶里的元素排序）
    def insertion_sort(bucket: List[int]) -> List[int]:
        for i in range(1, len(bucket)):
            current = bucket[i]
            pre_index = i - 1
            while pre_index >= 0 and current < bucket[pre_index]:
                bucket[pre_index + 1] = bucket[pre_index]
                pre_index -= 1
            bucket[pre_index + 1] = current

        return bucket

    # 固定桶数量为10
    bucket_num = 10
    buckets = [[] for _ in range(bucket_num)]

    min_value = min(arr)
    max_value = max(arr)
    data_range = max_value - min_value

    # 处理所有元素相同的情况避免data_range为0
    if data_range == 0:
        return arr

    # 元素分桶
    for num in arr:
        # 计算元素对应桶的索引
        index = int(((num - min_value) / data_range) * bucket_num)
        # 确保索引不超过最大值（num为max_value时，index为bucket_num，无法访问桶）
        index = min(index, bucket_num - 1)
        buckets[index].append(num)

    # 对每个桶执行插入排序
    for bucket in buckets:
        if len(bucket) > 0:
            insertion_sort(bucket)

    # 合并桶数据到原数组
    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

    return arr


# 10.
