# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 14:14
# @Author  : Gaocx
# @Email   : gaocaixin@kavout.com
# @File    : test
# @Desc    : xx

def minInt(num1, num2):
    return num1 if num1 < num2 else num2

def initManacher(s):
    sToChar = ['' for _ in range(2*len(s)+3)]
    print(len(s))
    # i = 0
    sToChar[0] = '@'
    sToChar[2*len(s)+2] = '$'
    for i in range(len(s)):
        sToChar[2*(i+1)]= s[i]
        sToChar[2*(i+1)-1]='#'
    sToChar[2*len(s)+ 1]='#'
    return sToChar

def mancher(s):
    i = 0
    sConvertion = initManacher(s)
    LArray = [0 for _ in range(2*len(sConvertion)+1)]
    # for i in range(5000):
    #     LArray[i] = 0
    id = 0
    mxId = 0
    for i in range(1,len(sConvertion) - 1):
        LArray[i] = min(LArray[2*id - 1],mxId -i) if mxId > i else 1
        while (sConvertion[i+LArray[i]] == sConvertion[i-LArray[i]]):
            LArray[i] += 1
        if((i+LArray[i]) > mxId):
            mxId = i + LArray[i]
            id = i
    maxLA = 0
    for i in range(1,len(sConvertion)):
        if LArray[i]>maxLA:
            LArray[0] = i
            maxLA = LArray[i]
    print(LArray[LArray[0]]-1)
    # print(((LArray[0]//2-1)-(LArray[LArray[0]]-1)//2+1))
    # print(((LArray[0]//2-1)+(LArray[LArray[0]]-1)//2+1))
    return s[((LArray[0]//2-1)-(LArray[LArray[0]]-2)//2):((LArray[0]//2-1)+(LArray[LArray[0]]-2)//2+1)] \
        if LArray[0]%2==0 \
        else s[((LArray[0]//2-1)-(LArray[LArray[0]]-1)//2+1):((LArray[0]//2-1)+(LArray[LArray[0]]-1)//2+1)]
if __name__ == '__main__':
    print(mancher('abbao'))