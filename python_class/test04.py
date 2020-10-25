# list1 = [True,200,33,"颜色",[1,2,3]]
# num=0
# for i in list1:
#     print(i)
#     num += 1
# print(num)
# dict1 = dict(name = "朵朵",age = 18,hobby = "看书")
# for j in dict1:
#     print(j)    #字典取出来的是key
#     print(dict1.get(j))  #通过key取到value值


# list1 = [True,200,33,"颜色",[1,2,3]]
# for i in list1:
#     if i == 33:
#         # break  #终止整个循环
#         continue #跳出本次循环
#     print(i)


# for i in range(3,6,1):  #从3开始取，到6结束，步长为1
#     print(i)
# for j in range(1,3):  #从1开始，到3结束，步长默认为1
#     print(j)
# for n in range(4):  #开始默认为0，结束为，步长默认为1
#     print(n)

# def add(count,defa = 500,*tuple1,**dict1):
#     sum = defa
#     for i in range(count+1):  #生成整数序列
#         sum += i
#     for j in tuple1:   #不定长参数，元组保存数据。传参的方式———位置传参
#         print(j)
#         sum += j
#     for info in dict1:
#         print(dict1.get(info))
#         sum += dict1.get(info)
#     return sum
# result = add(2,1000,2000,k = 5000,g = 600)  #count=2,defa=1000,tuple=(2000)
# print(result)


'''
1.把字符串转成列表 —— list()

2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
'''

# str1 = "好好学习，天天向上"
# list1 = list(str1)
# print(list1)

# def add(stop,start=0,step=1):
#     list1=[]
#     sum = 0
#     for i in range(start,stop,step):
#         sum += i
#         list1.append(i)
#     return list1,sum
# result = add(6,1,2)
# print("{}的所有数字和为{}".format(result[0],result[1]))


def len_5(*obj1,**obj2):
    if len(obj1)+len(obj2) > 5:
        return True
    else:
        return False
result = len_5(14,56,89,"kdsijd",a=5,b="sdaaw")
print(result)