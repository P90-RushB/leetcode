# 堆的每个父节点都大于孩子节点。
# 堆是一种完全二叉树（从左到右，上到下没空隙）
# 堆提供了很有限的几个操作：主要就插入和移除。
# 插入函数add需要_siftup,
# 移除函数extract需要_siftdown。

# 实现一个最大堆：
class MaHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = [0] * maxsize
        self._count = 0

    def __len__(self):
        return self._count
    
    # 加元素操作比较简单，就是加到末尾，然后地柜调用_siftup,满足条件就继续上浮。不说了。
    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, idx):
        # 递归进行，一直往上挪。

        # idx大于0，就还有父节点，就继续递归
        if idx > 0:
            parent = int((idx-1) // 2)
            if self._elements[idx] > self._elements[parent]:
                self._elements[idx], self._elements[parent] = self. _elements[parent], self._elements[idx]
                self._siftup(parent)

    # 难点就在于去除元素的操作。
    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        # 抽取的开头元素。
        value = self._elements[0]
        # 有效数组长度减一
        self._count -= 1
        # 将最后一个有效元素挪到开头位置。因为_count-1了，后面留着的数据也用不到了，垃圾值。
        self._elements[0] = self._elements[self._count]
        # 开始核心操作，递归下沉数据。
        self._siftdown(0)
        return value

    # 取数据的核心操作。这个是我的写法，因为看python163的写法太不直觉了，不如自己这个容易理解。
    # 传入的idx是当前要下沉的元素的序号。
    def _siftdown(self, idx):
        # n代表了有效数组最后一个元素的索引序号。
        n = self._count - 1
        # 根据公式，得到最后一个有效元素的父节点的索引：（n-1）//2
        # 如果当前idx索引小于等于最后一个父节点，说明还有继续下沉的可能，
        # 否则就是地柜出口
        if (n - 1) // 2 >= idx:
            # 得到idx的左和右子节点的索引位置。
            left = idx * 2 + 1
            right = idx * 2 + 2
            # 如果右子节点的位置是在最后一个有效索引n之前，说明idx是有右子节点的
            if right <= n:
            # 就需要堆idx的左右判断，找最大的值的序号给largest
                largest = left if self._elements[left] >= self._elements[right] else right
            # 否则说明idx没有右子节点（那其实idx就是最后一个父节点且只有左子节点的情况）
            else:
                largest = left
            
            # 这里想明白，找到左右子节点的最大值largest之后，
            # largest位置的值可并不一定比idx的值要大，也就不一定要继续siftdown了
            # 如果画个图看，就是从顶开始下沉，沉到一半就不用再沉了。
            # 举个例子：原_elements数组： [100, 40, 50, 30, 20, 5, 1, 10]
            # 将100去掉，10补到开头之后，看看。所以这个if还是要的。
            if self._elements[largest] > self._elements[idx]:
                self._elements[largest], self._elements[idx] = self._elements[idx], self._elements[largest]
                self._siftdown(largest)

def test_maxheap():
    import random
    n = 5
    h = MaHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        print(i)
        assert i  == h.extract()
    print('ok')

# test_maxheap()

# 写好了堆，自然就有堆排序了。
# 来一个倒序排序
def heapsort_reverse(array):
    lgh = len(array)
    maxheap = MaHeap(lgh)
    for i in array:
        maxheap.add(i)

    res = []
    for i in range(lgh):
        res.append(maxheap.extract())
    return res

def test_heapsort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    print(heapsort_reverse(l))
    assert heapsort_reverse(l) == sorted(l, reverse=True)

# test_heapsort_reverse()


############## 下面看看Python自带的heapq模块，heapq模块只提供了一个最小堆。
# 那这里有一个技巧，就是用最小堆实现最大堆的功能（或者反过来）
# 其实很简单， 原数据序列放入最大堆 = 原数据序列的每个元素取相反数放入最小堆
# 这样就能用最小堆实现最大堆的功能了，只需要在加入元素时对原数据取反，取出来后再取反一次，恢复数据即可。

# 一个对heapq的介绍：https://www.jianshu.com/p/801318c77ab5
# 需要注意的是python没有提供 堆 这个类型，而是对堆操作的几个函数，操作的堆是用list表示的。
#             函 数                                                           描 述
#     heappush(heap, x)                                        将x压入堆中
#     heappop(heap)                                      从堆中弹出最小的元素
#     heapify(heap)                                           让列表具备堆特征
# heapreplace(heap, x)                            弹出最小的元素，并将x压入堆中
#     nlargest(n, iter)                                       返回iter中n个最大的元素
#     nsmallest(n, iter)                                   返回iter中n个最小的元素

# 下面就用heapq（最小堆）来实现上面的最大堆功能。
def test_use_heapq_maxheap():
    import random
    import heapq
    l = list(range(10))
    random.shuffle(l)
    maxheap = []
    
    for i in l:
        heapq.heappush(maxheap, -i)
    n = len(l)
    res = [-heapq.heappop(maxheap) for _ in range(n)]
    print(res)
    assert res == sorted(l, reverse=True)

test_use_heapq_maxheap()


# 最后，堆还能实现快速找前（注意，是前k大的都能找到）k大数（或第k小数的）功能。而如果只需要找到第K大，
# 最高效的方式是利用快排中的partition函数的思想
# （partition的方法在快排那个代码中有说。）
# 用堆解决topk. 仔细想想，如果解决第k大，要用最小堆；反之，用最大堆。

import heapq
class TopK:
    """获取大量元素 topk 大个元素，固定内存
    思路：
    1. 先放入元素前 k 个建立一个最小堆
    2. 迭代剩余元素：
        如果当前元素小于堆顶元素，跳过该元素（肯定不是前 k 大）
        否则替换堆顶元素为当前元素，并重新调整堆
    """
    
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap
    
def test():
    import random
    i = list(range(1000))
    random.shuffle(i)
    topk = TopK(i, 10)
    print(topk.get_topk())

if __name__ == '__main__':
    test()


