#其实列表就是用中括号 [] 括起来的数据，里面的每一个数据就叫做元素。每个元素之间使用逗号分隔。
list1 = ['两点水','twowter','liangdianshui',123]
print(list1)

#访问列表中的元素
name = ['一点水', '两点水', '三点水', '四点水', '五点水']
# 通过索引来访问列表
print(name[2])                           #这是因为在编程世界中，都是从0开始的，而不是我们生活习惯中从1开始。
# 通过方括号的形式来截取列表中的数据
print(name[0:2])                         #那是因为这是**左闭右开**区间的。所以’name[0:2]‘的意思就是从第0个开始取，取到第2个，但是不包含第2个。

print(name[0:2])
print(name[:2])          #=print(name[0:2])
print(name[:])           #=print(list1)
print(name[1:2])
print(name[0:3])

#怎么去更新 List（列表）
#通过索引对列表的数据项进行修改或更新
name[1] = '2点水'
print(name)
#使用append()方法来添加列表项
name.append('六点水')
print(name)

#怎么删除 List（列表）里面的元素
name = ['一点水', '两点水', '三点水', '四点水', '五点水']
print(name)
# 使用 del 语句来删除列表的的元素
del name[3]
print(name)

#列表的运算
#列表对`+`和`*`的操作符与字符串相似。`+`号用于组合列表，`*`号用于重复列表。
listnumber1 = [1,2,3]
listnumber2 = [4,5,6]
print(len(listnumber1), listnumber1)
print(len(listnumber2), listnumber2)
listnumber3 = listnumber1 + listnumber2
print(len(listnumber3), listnumber3)

liststr = ['hi']
print(len(liststr), liststr)
liststr = liststr * 3
print(len(liststr), liststr)

#判断元素是否存在于列表中
print(3 in listnumber3, 4 not in listnumber3)

#分别输出列表中的所有元素
for x in listnumber1:
    print(x)

#List（列表）函数&方法
list0 = [1,1,5,7,2,2,3,4,5,6,7,8,9,0]
tup0 = (2,4,6,67,2)
print(len(list0))            #列表元素个数
print(max(list0))            #返回列表元素最大值
print(min(list0))            #返回列表元素最小值
print(list(tup0))            #将元组转换为列表
list0.append(10)             #在列表末尾添加新的对象
print(list0)
print(list0.count(1))        #统计某个元素在列表中出现的次数
list0.extend(tup0)           #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(list0)
print(list0.index(5))        #从列表中找出某个值第一个匹配项的索引位置
list0.insert(5, 4)           #将对象插入列表
print(list0)
list0.pop(3)                 #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list0)
list0.remove(5)              #移除列表中的一个元素（参数是列表中元素），并且不返回任何值
print(list0)
list0.reverse()              #反向列表中元素
print(list0)
list0.sort()                 #对原列表进行排序
print(list0)