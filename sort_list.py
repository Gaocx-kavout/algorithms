# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 19:22
# @Author  : Gaocx
# @Email   : gaocaixin@kavout.com
# @File    : select_sort
# @Desc    : 排序

### 冒泡排序
# 原理 前后相邻两个数 大的和小的交换位置

def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(1,len(li)):
            if li[j] < li[j-1]:
                li[j],li[j-1] = li[j-1],li[j]
    return li

def bubble_sort_with_flag(li):
    # 如果内层循环时候发现一次都没有执行交换则说明后续的有序，直接返回
    for j in range(len(li)-1):
        flag = False
        for i in range(1, len(li)):
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
                flag = True
        if not flag:
            return li
    return li

### 插入排序
# 把列表分为有序区和无序区两个部分。最初有序区只有一个元素。
# 然后每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。

def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and tmp < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
    return li

### 选择排序 遍历一遍拿最小的放到第一位置再拿剩下的找到最小的放到第二位置

def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i],li[min_loc] = li[min_loc],li[i]
    return li

### 快速排序法
# 原理 让指定的元素归位，所谓归位，
# 就是放到他应该放的位置（左变的元素比他小，右边的元素比他大），
# 然后对每个元素归位，就完成了排序
def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        print(data)
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
        print(data)
    data[left] = tmp
    print(data)
    return left

def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)
    return data

### 归并排序
# 归并排序原理
# 列表分成两段有序，然后分解成每个元素后，再合并成一个有序列表，这种操作就叫做一次归并

# 应用到排序就是，把列表分成一个元素一个元素的，
# 一个元素当然是有序的，将有序列表一个一个合并，'
# 最终合并成一个有序的列表

def merge(li, left, mid, right):
    # 一次归并过程 把从mid分开的两个有序列表合并成一个
    i = left
    j = mid + 1
    ltmp = []
    # 两个列表的元素依次比较
    while i <= mid and j <= right:
        # print('92',i,j,mid,li,ltmp)
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # 因为两个列表可能不是均分的而且他们的值在上边循环的时候会差一些
    # 所以下边添加上
    while i <= mid:
        # print('02',i,j,mid,li,ltmp)
        ltmp.append(li[i])
        i += 1
    while j <= right:
        # print('06',i,j,mid,li,ltmp)
        ltmp.append(li[j])
        j += 1
    # print(left,right+1,mid,li,ltmp)
    li[left:right+1] = ltmp
    return li

def _merge_sort(li, left, right):
    if left < right:
        mid = (left + right)//2
        _merge_sort(li, left, mid)
        _merge_sort(li, mid+1, right)
        merge(li, left, mid, right)
    return li

def merge_sort(li):
    return _merge_sort(li, 0, len(li)-1)


### 堆排序
# 排序原理
"""
# 堆 堆是一类特殊的树，要求父节点大于或小于所有的子节点
堆的调整：当根节点的左右子树都是堆时，可以通过一次向下的调整来将其变换成一个堆。
    所谓一次向下调整，就是说把堆顶的值，向下找一个合适的位置，
是一次一次的找，跟他交换位置的值，也要找到一个合适的位置

堆排序的过程
　　1.构造堆
　　2.得到堆顶元素，就是最大的元素
　　3.去掉堆顶，将堆的最后一个元素放到堆顶，此时可以通过一次调整重新使堆有序
　　4.堆顶元素为第二大元素
　　5.重复步骤3，直到堆为空
"""
def sift(li, left, right):
    # 构造堆
    i = left  # 作为根节点
    j = 2 * i + 1 # 子节点的下标
    tmp = li[left]
    while j <= right:
        if j+1 <= right and li[j] < li[j+1]: # 如果j+1没有越界而且li[j] < li[j+1]
            j += 1                            # 找到两个节点中大的那个的下标
        if tmp < li[j]: # 比较根节点和子节点中较大节点的大小，根节点小的话交换
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            break
    li[i] = tmp

def heap_sort(li):
    n = len(li)
    for i in range(n//2-1,-1,-1):
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0],li[i] = li[i],li[0]
        sift(li,0, i-1)
    return li

### 使用heapq模块
#队列中的每个元素都有优先级，优先级最高的元素优先得到服务（操作），
# 这就是优先队列，而优先队列通常用堆来实现
import heapq
def heapq_sort(li):
    n = []
    for i in li:
        heapq.heappush(n,i)
    return [heapq.heappop(n) for _ in range(len(li))]

# 扩展
## 希尔排序
# 希尔排序是一种分组插入排序的算法　　

# 思路：
#
# 　　首先取一个整数d1=n/2，将元素分为d1个组，每组相邻量元素之间距离为d1，
# 在各组内进行直接插入排序；
#
# 　　取第二个整数d2=d1/2，重复上述分组排序过程，直到di=1，
# 即所有元素在同一组内进行直接插入排序。
#
# 希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；
# 最后一趟排序使得所有数据有序。

def shell_sort(li):
    gap = int(len(li)//2)   # 初始把列表分成 gap个组，但是每组最多就两个元素，第一组可能有三个元素
    while gap >0:
        for i in range(gap,len(li)):
            tmp = li[i]
            j = i - gap
            while j>0 and tmp<li[j]:    # 对每一组的每一个数，都和他前面的那个数比较，小的在前面
                li[j+gap] = li[j]
                j -= gap
            li[j+gap] = tmp
        gap = int(gap//2)
    return li



if __name__ == '__main__':
    # li = [i for i in range(100)]
    # li.reverse()
    # print(bubble_sort(li))
    # print(bubble_sort_with_flag(li))
    # print(insert_sort(li))
    # print(select_sort(li))
    li = [10,4,6,3,8,2,5,7]
    print(li)
    # print(quick_sort(li, 0, len(li)-1))
    # print(merge_sort(li))
    print(heap_sort(li))
    print(heapq_sort(li))