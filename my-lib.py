# -*- coding: utf-8 -*-
"""
    my-lib.py
"""
# 九九乘法表
def print_nn():
    
    for i in range(1, 10):
        for j in range(1, 10):
            print format(i * j,"3"),
        print #打印换行

# 鸡兔同笼
# 1. 穷举法
def chicken_and_rabbit():
    
    for c in range(36):
        for r in range(36):
            if 2 * c + 4 * r == 94 and c + r == 35:
                print c, r

# 判断素数
def is_prime(n):
    
    for i in range(2, n):
        if n % 2 == 0:
            return False
    else:   #当循环非正常结束时执行
        return True

# 数字逆转， 比如123 输出321
def num_reverse(n):
    
    res = 0
    while n !=0:
       res = res * 10 + (n % 10)
       n = n / 10

    return res

# 阶乘 1x2x3x4...n
def p(n):
    x = 1
    i = 1
    while(i <= n):
        x = x * i
        i = i + 1
    return x

# 斐波那契数列
def fib(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 汉诺塔 A,B,C三个盘子大小A<B<C
count = 0
def hanoi(n, A, B, C):
    global count
    if n == 1:
        print "Move", n, "from", A, "to", C
        count += 1
    else:
        hanoi(n-1, A, C, B)
        print "Move", n, "from", A, "to", C
        count += 1
        hanoi(n-1, B, A, C)

# 人名游戏，读取人名列表，将每个人的首字母大写，其余的小写
def name_game():
    
    f = open("names.txt")
    for line in f:
        line = line.strip()
        print line.title()
    f.close()

# 列表中值的交换
def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp


# 列表查找 (线性查找)
def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    
    return -1   #执行完循环都没有查找到，返回-1

# 二分查找 (要求从小到大的有序列表)
def bi_search(lst, x):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) / 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

#选择排序 v1 (在列表中插入删除的操作比较耗时)
#1. 找到最小的元素
#2. 删除它，然后插入相应的位置
#3. 重复步骤1和2
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        #开始插入
        lst.insert(i, lst.pop(min_index))

#选择排序 v2 时间复杂度O(n*n)
#1. 找到最小的元素
#2. 和第一个元素交换
#3. 重复步骤1和2
def selection_sort_v2(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        #开始交换 lst[i] 和 lst[min_index]
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp

#冒泡排序 (比选择排序要快，虽然时间复杂度一样)
#与选择排序类似，但每次遍历不止交换一次
#每次遍历，将最大值排列在最后
#一旦排好序，算法可以停止
def bubble_sort(lst):
    top = len(lst) - 1
    is_exchanged = True
    while is_exchanged:
        is_exchanged = False
        for i in range(top):   #查找最大的元素
            if lst[i] > lst[i+1]:
                is_exchanged = True
                #交换
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp           
        top -= 1

#元组(即不可变的列表) 同时返回最大最小值
def max_min(lst):
    max = min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

#将单词根据长度排序
def word_sortby_len():
    
    lst = ['abc', 'defg', 'ab', 'abccc']
    lst.sort(key = lambda x: len(x), reverse = True)
    print lst

#判断字符串，字母出现的次数
def word_times():
    
    s = 'abcchelloconfidence'
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    print dic

#字典翻转
#同一个值可能对应多个键，需要用到列表储存
def dict_reverse():
    
    d1 = {'Bob': 101, 'Tim': 121, 'Sara': 101, 'Ting': 133}
    d2 = {}
    
    for name, room in d1.items():
        if room in d2:
            d2[room].append(name)
        else:
            d2[room] = [name]
    
    print d2
            


                
  