import random

# 检查各排序算法是否正确
def test_sort(method):
    seq = list(range(10))  
    random.shuffle(seq)
    method(seq)
    assert seq == sorted(seq) 

#  冒泡
# def bubble_sort(seq):
#     print('before sort:', seq)
#     n = len(seq)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if seq[j] > seq[j+1]:
#                 seq[j], seq[j+1] = seq[j+1], seq[j]
#         print(seq)
    
# 选择排序

#  一种非常不高效的不推荐的方式：每个与开头比，小了就换，小了就换，如下
# def select_sort(seq):
#     n = len(seq)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if seq[i] > seq[j]:
#                 seq[i], seq[j] = seq[j], seq[i]
#     print(seq)

# 而真正的选择排序，每遍历一轮，才交换一次，这才高效。遍历过程中记录最大值的索引即可。
# def select_sort(seq):
#     print('before sort:', seq)
#     n = len(seq)
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if seq[min_idx] > seq[j]:
#                 min_idx = j
#         if min_idx != i:
#             seq[i], seq[min_idx] = seq[min_idx], seq[i]
#         print(seq)



# 插入排序, 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素。
def insert_sort(seq):
    n = len(seq)
    print('before sort:', seq)
    for i in range(1, n):
        # 把i位置的索引和值拿出来，这才是插入排序的精髓。
        # 就是把一张牌拿起来，但还没有放到一堆牌中，
        # 所以插入排序并不会几个数频繁交换，只会找准位置插一次。
        # 而每次比较时，被比较的那个值会移动，留下一个空槽。
        # 最后，把手头的那张牌插入空槽。
        # 比较的时候当然不是拿空槽比，所以while里不是比
        # seq[pos]和seq[pos-1]，而是value(手头的牌)和
        # 空槽前一位seq[pos-1]
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value
        print(seq)

# test_sort(bubble_sort)
# test_sort(select_sort)
test_sort(insert_sort)