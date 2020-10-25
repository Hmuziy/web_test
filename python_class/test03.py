'''
取值
# list1 = [True,200,33,"颜色",[1,2,3]]
# print(list1)
# print(list1[2])
# print(list1[0:2:1])
# print(list1[-1][1])
'''

# #增加
# list1 = [True,200,33,"颜色",[1,2,3]]
# print(list1)
# list1.append("红色") #默认添加在末尾
# print(list1)
# list1.insert(1,"蓝色") #指定位置添加
# print(list1)
# list1.extend([555,666])  #添加多个元素---列表合并
# print(list1)

# #删除
# list1 = [True,200,33,"颜色",[1,2,3]]
# print(list1)
# list1.pop()  #默认删除最后一个
# print(list1)
# list1.pop(0) #删除指定位置
# print(list1)
# list1.remove("颜色") #删除指定元素
# print(list1)

# # 修改
# list1 = [True,200,33,"颜色",[1,2,3]]
# print(list1)
# list1[0]=False
# print(list1)


# #元组取值
# tuple1=(100,200,300,"小红花",(1,2,3))
# print(tuple1[1])
# print(tuple1[1:3:1])
# print(tuple1[-1][2])

# #修改
# tuple1=(100,200,300,"小红花",(1,2,3))
# list1=list(tuple1)
# list1[1]="奖励"
# tuple2=tuple(list1)
# print(tuple2)


#字典
# dict1={"name":"点点","age":18,"gender":"male"}
# print(dict1["name"])
# print(dict1.get("name"))
# dict1["name"] = "花花" #修改name的值
# dict1["hobby"] = "看书" #key不存在，则新增键值对
# print(dict1)
# dict1.update({"age":20,"hobby":"运动"})
# print(dict1)
# dict1.pop("name")
# print(dict1)


# a=[1,2,'6','summer']
# print("i" in a)

# dict_1={"class_id":45,'num':20}
# if dict_1["num"]>5:
#     print("班级上课人数为{}".format(dict_1["num"]))
# else:
#     print("班级上课人数不大于5")


# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
# 并且把字典都存在新的 list中，最后打印最终的列表。
# 方法1： 手动扩充--字典--存放在列表里面；
# 方法2： 自动--dict（）


# dict1 = {"姓名":list1[0],"性别":"男","年龄":19,"城市":"北京"}
# dict2 = {"姓名":list1[1],"性别":"女","年龄":18,"城市":"上海"}
# dict3 = {"姓名":list1[2],"性别":"女","年龄":19,"城市":"杭州"}
# dict4 = {"姓名":list1[3],"性别":"男","年龄":20,"城市":"深圳"}
# dict5 = {"姓名":list1[4],"性别":"女","年龄":22,"城市":"北京"}
# dict6 = {"姓名":list1[5],"性别":"男","年龄":21,"城市":"广州"}
# list2 = list(dict1.values()),list(dict2.values()),list(dict3.values()),list(dict4.values()),list(dict5.values()),list(dict6.values())
# for list3 in list2:
#     print(list3)

list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
list3 = ['男', '女', '女', '男', '女', '男']
list4 = ['19', '18', '19', '20', '22', '21']
list5 = ['北京', '上海', '杭州', '深圳', '北京', '广州']
for i in range(6):
    dict7 = dict(姓名=list1[i], 性别=list3[i], 年龄=list4[i], 城市=list5[i])
    print(list(dict7.values()))