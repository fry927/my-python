# -*- coding: utf-8 -*-
"""
    my-lib.py
"""
# 九九乘法表
#for i in range(1, 10):
#    for j in range(1, 10):
#        print format(i * j,"3"),
#    print

# 鸡兔同笼
# 1. 穷举法
#for chickens in range(36):
#    for rabbits in range(36):
#        if 2 * chickens + 4 * rabbits == 94 and chickens + rabbits == 35:
#            print "Numbers of chicken: ", chickens
#            print "Numbers of rabbit: ", rabbits

# 判断素数
#x = 7
#for i in range(2, x):
#    if x % 2 == 0:
#        print x, " is not prime"
#        break
#else:   #当循环非正常结束时执行
#    print x," is prime"
#

# 数字逆转， 比如123 输出321
# num = 123
# num_reverse = 0
# while num !=0:
#    num_reverse = num_reverse * 10 + (num % 10)
#    num = num / 10
#
# print 'reverse num is ', num_reverse

# 阶乘 1x2x3x4...n
# def p(n):
#     x = 1
#     i = 1
#     while(i <= n):
#         x = x * i
#         i = i + 1
#     return x
#
# print p(4)

# 斐波那契数列
# def fib(n):
#     if(n == 1 or n == 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print fib(3)

# 汉诺塔 A,B,C三个盘子大小A<B<C
# count = 0
# def hanoi(n, A, B, C):
#     global count
#     if n == 1:
#         print "Move", n, "from", A, "to", C
#         count += 1
#     else:
#         hanoi(n-1, A, C, B)
#         print "Move", n, "from", A, "to", C
#         count += 1
#         hanoi(n-1, B, A, C)
#
# hanoi(2, "L", "M", "R")
# print 'Move times', count

# 人名游戏，读取人名列表，将每个人的首字母大写，其余的小写
#f = open("names.txt")
#for line in f:
#    line = line.strip()
#    print line.title()
#f.close()

# 列表中值的交换
#def swap(lst, a, b):
#    temp = lst[a]
#    lst[a] = lst[b]
#    lst[b] = temp
#lst = [10, 20]
#swap(lst, 0, 1)
#print lst

# 列表查找 (线性查找)
#def search(lst, x):
#    for i in range(len(lst)):
#        if lst[i] == x:
#            return i
#    
#    return -1   #执行完循环都没有查找到，返回-1
#
#lst = [1, 2, 5]
#print search(lst, 1)

# 二分查找 (要求从小到大的有序列表)
#def bi_search(lst, x):
#    low = 0
#    high = len(lst) - 1
#    
#    while low <= high:
#        mid = (low + high) / 2
#        if lst[mid] == x:
#            return mid
#        elif lst[mid] < x:
#            low = mid + 1
#        else:
#            high = mid - 1
#            
#    return -1
#
#lst = [1, 2, 5]
#print bi_search(lst, 5)

#选择排序 v1 (在列表中插入删除的操作比较耗时)
#1. 找到最小的元素
#2. 删除它，然后插入相应的位置
#3. 重复步骤1和2
#def selection_sort(lst):
#    for i in range(len(lst)):
#        min_index = i
#        for j in range(i+1, len(lst)):
#            if lst[j] < lst[min_index]:
#                min_index = j
#        #开始插入
#        lst.insert(i, lst.pop(min_index))
#
#lst = [19, 11, 3, 9, 2]
#selection_sort(lst)
#print lst

#选择排序 v2 时间复杂度O(n*n)
#1. 找到最小的元素
#2. 和第一个元素交换
#3. 重复步骤1和2
#def selection_sort_v2(lst):
#    for i in range(len(lst)):
#        min_index = i
#        for j in range(i+1, len(lst)):
#            if lst[j] < lst[min_index]:
#                min_index = j
#        #开始交换 lst[i] 和 lst[min_index]
#        temp = lst[i]
#        lst[i] = lst[min_index]
#        lst[min_index] = temp
#
#lst = [19, 11, 22, 9, 2]
#selection_sort_v2(lst)
#print lst

#冒泡排序 (比选择排序要快，虽然时间复杂度一样)
#与选择排序类似，但每次遍历不止交换一次
#每次遍历，将最大值排列在最后
#一旦排好序，算法可以停止
#def bubble_sort(lst):
#    top = len(lst) - 1
#    is_exchanged = True
#    while is_exchanged:
#        is_exchanged = False
#        for i in range(top):   #查找最大的元素
#            if lst[i] > lst[i+1]:
#                is_exchanged = True
#                #交换
#                temp = lst[i]
#                lst[i] = lst[i+1]
#                lst[i+1] = temp           
#        top -= 1
#            
#lst = [19, 1, 22, 9, 2]
#bubble_sort(lst)
#print lst


                
  