from typing import List

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


if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(counting_sort(test_array))