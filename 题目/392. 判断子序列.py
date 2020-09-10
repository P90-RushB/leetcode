class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 方法一
        # 两个指针指向s，t。如果字符相等，各自自增，不等，就只有t的自增。最后看遍历到的
        # s的位置是否是s末尾。
        # i = 0
        # j = 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)


        # 自己写的，不简洁，看上面的
        # 就对s的每个，如果t里有就继续。
        # idx_t = 0
        # lgh = len(t)
        # for i in s:
        #     go_on = False
        #     while idx_t < lgh:
        #         if i in t[idx_t]:  
        #             idx_t += 1                  
        #             go_on = True
        #             break
        #         idx_t += 1
        #     if not go_on:
        #         return False

        # return True



        # follow up思考
        # 建立t中每个字符与其位置之间的映射，也就是一个字典：
        # 每个字符：其所处的位置的数组。
        # 对每个s中的字符c，在字典中找（用二分加快速度）
        # 并且不仅仅是c in 指定数组就行，还要记录当前t中的位置pre，如果在
        # pre 之前，那肯定不行。
        dic = defaultdict(list)
        for k,v in enumerate(t):
            dic[v].append(k)
        
        # pre代表一个目标值，在s中遍历到的每个c，在dic中对应的dic[c]
        # 这个数组，其中要有值大于pre. 并且用大于pre的第一个值来更新pre
        # pre代表了在s中上一次遍历到的字符，对应在t中的序号。
        # 当前的字符c不仅要在dic中，并且dic[c]数组中，要有至少一个序号
        # 要大于pre，因为是由顺序的。
        pre = -1

        # def upper_bound(i, pre):
        #     nonlocal dic

        #     for t in dic[i]:
        #         if t > pre:
        ## 如果找到大于pre的数就返回该数，否则返回-1
        #             return t
        #     return -1

        # 二分查找upper_bound
        def upper_bound(i, pre):
            nonlocal dic
            left = 0 
            right = len(dic[i]) -1
            while left <= right:
                mid = left + (right-left ) // 2
                if dic[i][mid] > pre:
                    right = mid - 1
                else:
                    left = mid + 1
            # 如果left都大于最后一个数的索引了，说明没有大于pre的数，返回-1
            if left == len(dic[i]):
                return -1
            # 否则返回找到的pre的upper_bound
            else:
                return dic[i][left]

        for c in s:
            # 如果c不在dic中，当然直接就Flase
            if c not in dic:
                return False
            else:
                idx = upper_bound(c, pre)
                if idx == -1:
                    return False
                pre = idx
        return True
