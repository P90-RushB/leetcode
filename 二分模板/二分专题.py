# 我的二分查找模板，以下描述参考自： https://www.acwing.com/blog/content/31/
# 二分模板一共有两个，分别适用于不同情况。
# 算法思路：假设目标值在闭区间[l, r]中， 每次将区间长度缩小一半，当l = r时，我们就找到了目标值。

# 二分查找的写法不唯一，可以变动的地方有
# 1. right初始化，可以为len(nums)或（nums）-1
# 2. left和right的关系，可以写成left < right 或left <= right
# 3. right的更新，可以写成right = mid 或者 right = mid -1
# 4. 最后的返回值，可以返回left, right或right - 1

# 但是！！！！！！！！！！！！，上面四类可选的情况并不能任意组合
# 所以，记住自己习惯的一个模板就好。

# 以下经验来自：https://www.cnblogs.com/grandyang/p/6854825.html
# 但是这些不同的写法并不能随机的组合，像博主的那种写法，若 right 初始化为了 
# nums.size()，那么就必须用 left < right，而最后的 right 的赋值必须用 right = mid。
# 但是如果我们 right 初始化为 nums.size() - 1，那么就必须用 left <= right，并且right
# 的赋值要写成 right = mid - 1，不然就会出错。所以博主的建议是选择一套自己喜欢的写法，并且记住

def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

# 我以后就用这个模板啦，用end为数组长度减一这个
    beg = 0
    end = len(sorted_array) - 1

    # 对于初始化时end为长度减一的写法，独赢的，循环中就要用 <=
    while beg <= end:
        # 各语言通用的算mid时防止数值溢出的写法。
        mid = beg + (end - beg) // 2
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

    # 总结：我用的模板：end为长度减一，对应的，循环要用beg<=end, 对应的end = mid -1，beg = mid + 1

# 以上是四大情形中的第一种：查找和目标值相等的数所在的索引。
# 例子：367. 有效的完全平方数(最直观，就是二分第一种应用) 349.两个数组的交集 

# 第二个情形：查找第一个不小于目标值的数，可变形为查找最后一个小于目标值的数
# 这是比较常见的一类，因为我们要查找的目标值不一定会在数组中出现，也有可能是跟目标值相等的数在数组中并不唯一，
# 而是有多个，那么这种情况下 nums[mid] == target 这条判断语句就没有必要存在。
# 比如在数组 [2, 4, 5, 6, 9] 中查找数字3，就会返回数字4的位置；在数组 [0, 1, 1, 1, 1] 
# 中查找数字1，就会返回第一个数字1的位置。

 # 方法二: 找最后一个小于target的数的序号, 或者第一个大于target的数的序号。
        # 由于我用的模板是《=，mid+1，mid-1，这种，在结束时，
        # 如果用right作为返回值，由于返回的是mid -1，所以right已经代表了最后一个小于target的序号。
        # 而如果返回left，由于left = mid + 1，所以已经代表第一个大于target的序号。
        # 例子：441. 排列硬币
def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

    left = 0
    right = len(sorted_array) - 1

    while left <= right:
        # 各语言通用的算mid时防止数值溢出的写法。
        mid = left + (right - left) // 2
        if sorted_array[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    # 如果返回的是right，代表最后一个小于目标值的数的序号。
    # 如果返回left，就是第一个大于目标值的数的序号。
    return right

    ##################### 方法二，找upper bound 或者lower bound 的更新 #################
    ################# 最清晰思路 #####################
    # 见题目 744. 寻找比目标字母大的最小字母
    # 关键就在于按照情况，分析何时写>= 或者<=
