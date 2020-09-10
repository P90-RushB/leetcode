# class Solution:
#     def nextGreatestLetter(self, letters, target):
#         dic = {}
#         for i in range(97, 123):
#             dic[char(i)] = i

#         n = len(letters)
#         tmp = [0] * n
#         for i in range(n):
#             tmp[i] = dic[letters[i]]

#         target = int(target)

#         if target > tmp[-1]:
#             return tmp[0]

#         left = 0
#         right = n - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if mid > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return left 
        
# s = Solution()
# res = s.nextGreatestLetter(["c","f","j"], 'a')
# print(res)

print('c' > 'a')