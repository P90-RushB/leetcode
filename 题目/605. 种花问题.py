class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        # 防御性编程，左右各加一个0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        m = len(flowerbed)
        for i in range(1, m-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0 : return True
        return False

        # 我自己写的，好麻烦…… 用上面的防御性编程思想，左右各加一个0
        # 就遍历看，每当一个空位置左右都是空，就可以插。
        # m = len(flowerbed)
        # if m < 2:
        #     if n!=0 and (m == 0 or (m == 1 and flowerbed[0] == 1)):
        #         return False
        #     else:
        #         return True

        # # 至少有俩数。 
        # for i in range(m):
        #     if i == 0:
        #         if flowerbed[i] == 0 and flowerbed[i+1] == 0:
        #             flowerbed[i] = 1
        #             n -= 1
        #     elif i == m-1:
        #         if flowerbed[i] == 0 and flowerbed[i-1] == 0:
        #             flowerbed[i] = 1
        #             n -= 1
        #     else:
        #         if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        #             flowerbed[i] = 1
        #             n -= 1
        #             if n <= 0:
        #                 return True
        # return True if n <= 0 else False