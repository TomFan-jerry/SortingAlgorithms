from typing import List

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


if __name__ == '__main__':
    test_array = [34, -5, 0, 12, 45, 7, -23, 19, 56, 3, 67, -12, 88, 5, 5, 0]
    print(bucket_sort(test_array))