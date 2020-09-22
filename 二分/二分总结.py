二分，思路简单，但是细节简直令人发指。
二分，又极其常用，尤其处理大数据时。因此，必须掌握。

几个讲解详细的博客：
1. labuladong的二分专题： https://github.com/labuladong/fucking-algorithm/blob/master/算法思维系列/二分查找详解.md
2. https://www.cnblogs.com/grandyang/p/6854825.html
3. leetcode官方的二分专题： https://leetcode-cn.com/explore/learn/card/binary-search/

################### 前言 ##################
二分的难点在于，什么时候用 right = len(nums) or right = len(nums) - 1,
相应的，要用 left < right or left <= right， 相应的right = mid - 1 or right = mid,
还有返回left 还是left - 1. 这些二选一不是随机组合的。

############## 第一类 寻找和目标值完全相同的数的索引位置 #############
# 这种是最基本的二分， 如果有多个连续的数和目标值相同，找到哪一个位置都有可能（这正是它的弱点）。
模板1：
def binarysearch(nums, target):
    if len(nums) == 0:
        return -1        
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 如果跳出while了，说明没找到。
    return -1

模板1分析：
    由于right初始化为len(nums) - 1，right是可以取到的，所以搜索区间是[left, right],即两端都闭。
    因此，while时为left <= right，因为当left == right时，仍不越界并需要判断target是否等于mid。
    又因为是两端都闭，当mid ！= target，就应该[left, mid-1] 或者[mid+1, right]中搜索，
    所以是left = mid + 1 or right = mid - 1
    局限：如果连续多个数等于目标值，并不能找到左或者右边界或者指定的第几个相等的位置等等高级搜索。

理解了 <=与<, ]还是），right = mid - 1 还是mid 这些逻辑之后，第一类应用当然也可以换用
while left < right的形式写。下面，看模板2. (一定要理解)
模板2 ## 万分重要 ###
def binarysearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0 
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left = mid + 1
        elif nums[mid] < target:
            right = mid # 一定要理解
    return -1

模板2分析：
    为什么这个模板万分重要呢，这体现了 right = len(nums) 还是len（nums）-1 及后续一系列不同
    的原因. 针对第一类找寻target位置的应用，模板1完全够用，但想进阶，一定要理解模板2.
    首先，由于right初始化为了len(nums)，该位置是取不到的，意味着搜索区间为[left, right）
    因为还是第一类找target的应用，所以当mid的值等于target，就返回，这没什么好说的；
    当mid值不等于target，由于mid已经判断过，并且区间为[left, right），则下一次搜索区间
    为[mid+1,right) 或者 [left，mid）.这也就是left = mid + 1 和 right = mid的原因。

################### 第二类 找等于target的数的左边界（有可能连续好几个等于target），
################### 可变形为找第一个不小于
################### target的数（大于等于都可以）， 也可变形为查找最后一个
################### 小于target的数
这种情况才是最常见的：等于target的数可能并不存在，或者存在，而且有连续多个。第一类并不能解决
连续多个中找指定的第几个这个问题。
下面首先以找等于target的数的左边界为例：
搜索左边界模板：
def binarysearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    if left == len(nums) or nums[left] != target:
        return -1
    else:
        return left
搜索左边界模板分析：
类似这种搜索左右边界等高级应用，一般用left < right这种方式（当然，用<=也
可以，详情见labuladong的博客）. 
首先，一定要注意第一类的模板2，与该方法是基本一致的。由于right = len(nums), right是取不到的，搜索区间
实际上是[left, right) 因此，采用left < right 的形式（因为left == right和[left, right) 肯定不能同时成立）
然后，和第一类模板2的分析一样，由于是左闭右开，当mid值不等于target，搜索区间会变为[mid+1,right) 或
[left，mid),因此，left = mid + 1, right = mid. 而与第一类的模板二不同的是，由于这个第二类应用不是单单找
等于target的数的位置，如果连续多个数等于target，找的是其左边界，则当nums[mid] == target时，不是直接返回，
而是right = mid，缩小右边界。则，有以下几种情况：
（1），target存在且不在左右边界：那么，由于right等于mid,一直缩小右边界，当mid不等时，left 又等于mid+1.
        最终找到的就是左边界（left == right， 返回哪个都行）
（2）target存在且在左边界：右边一直缩，直到等于left，也等于左边界。
（3）target存在且在右边界，左边一直 = mid + 1， 直到等于right, 也等于len（nums）-1（这种情况就只有一个数
    等于target了，才能到右边界）
（4）等于target的数不存在，while都跳出了，
    这时判断nums[left] != target，说明没找到。这也是需要额外判断的一个原因。注意，所有数都大于target
    也属于该情况，这时right会一直缩到第一个数，然后跳出。
（5）等于target的数不存在且target大于所有数。这种情况，left会一直等于mid + 1，直到等于right也等于
    len(nums)(因为right就没动过)，因此需要额外判断left == len(nums)时返回-1

这个所有情况的讨论只是为了证明这种写法是正确的，不用记。
需要注意的就是因为（4）和（5）情况，才需要两个额外判断：
if nums[left] != target left == len(nums): return -1

# 第二类的应用二：找最后一个小于target的数
很简单，上面找到第一个大于等于target的数，往前挪一位，完事。

# 第二类的应用三： 找第一个不小于target的数。
也就是如果不存在等于target的，就返回第一个大于target的。那这个也简单，
只要在模板的额外判断中，if nums[left] != target， 也返回left就完了。(也就是不要这个判断)


################## 第三类 找等于target的数的有边界， 可变形为
################## 找第一个大于target的数
第三类其实和第二类对比着来就行，一个找左边界，一个找右边界。
模板：
def binarysearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2 
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        if left == 0:
            return -1
        return left -1 if nums[left-1] == target else -1
    
 当target小于所有数，由于right一直左缩，最后left，right都等于索引0. 因此left == 0 代表没找到。
 当target等于第一个数，同样right一直缩，当缩到right等于索引1，left会等于mid+1 = 1，因此返回
 left-1 也是正确的。

 当target大于所有数，由于left不断变成mid+1，最后left = right = len(nums),
 当target是最后一个数，left也会left = right = len(nums).
 只要判断nums[left-1] 是否等于target。

 对于target不存在且大小处于序列中间，同样判断最后的nums[left-1] 是否等于target 即可。

 ###### 重要技巧 ##########
 第二类和第三类很像， 怎么不记错，一个返回left， 一个返回left-1 呢，
 实际上想返回的是mid，因此看nums[mid] == target的处理操作即可。第二类中，当nums[mid] == target时，
 right = mid 因此当搜索结束，left = right = mid，返回left。
 而第三类当nums[mid] == target时，left = mid + 1, 因此搜索结束时，left =right = mid + 1,
 所以返回left - 1

 # 第三类的应用二，找第一个大于target的数（注意，和找第一个大于等于target的数不同，大于等于说明
 # 找的是左边界），也就是找右边界再加1就完事。返回(left-1)+1即可。另外，因为target存不存在都行，所以
#  不用最后的额外判断。 这就是grandyang博客二分专题的第三类.
找第一个大于target 模板:
def binarysearch(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2 
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    return left


