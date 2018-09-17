# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 23:10
# @Author  : Gaocx
# @Email   : gaocaixin@kavout.com
# @File    : binary_search
# @Desc    : 二分查找法

import traceback
def binary_search(find, list_data):
    """
    二分查找方法
    :param find:要查找的值
    :param list_data: 总列表
    :return:  找到返回数据下标 找不到返回-1
    """
    low = 0
    high = len(list_data) - 1
    while low <= high:
        mid = (low + high)//2
        if list_data[mid] == find:
            return mid
        elif list_data[mid] > find:
            high = mid -1
        else:
            low = mid + 1
    return -1

lis_data = [i*i for i in range(200)]
lis_data.sort()
print(lis_data[0],'to',lis_data[-1],'length:',len(lis_data))
if __name__ == '__main__':
    while 1:
        find = input("请输入要查找的数：")
        if find.lower() == 'q':
            exit()
        try:
            find = int(find)
            result = binary_search(find, lis_data)
            if result != -1 :
                print("要找的元素%d的序号为：%d" %(find,result))
            else :
                print("未找到！")
        except:
            print(traceback.format_exc())
            print("请输入正整数！")