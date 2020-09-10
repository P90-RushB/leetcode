# 归并
# 该部分讲解还是直接看原版吧，很清楚：
# https://github.com/PegasusWang/python_data_structures_and_algorithms/blob/master/docs/13_高级排序算法/merge_sort.md

import random

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])

        # 合并两个有序数组
        new_seq = merge_sorted_list(left_half, right_half)
        return new_seq

def merge_sorted_list(sorted_a, sorted_b):
    len_a, len_b = len(sorted_a), len(sorted_b)
    # 双指针合并两个有序数组，常用套路
    a = b = 0
    new_sorted_seq = list()
    while a < len_a and b < len_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    if a < len_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    
    return new_sorted_seq


def test_sort(method):
    seq = list(range(10))  
    print('before sort:',seq)
    random.shuffle(seq)
    after_sort = method(seq)
    print('after sort:', after_sort)
    assert after_sort == sorted(seq) 

test_sort(merge_sort)

