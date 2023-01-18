'''
3.压缩列表求积
1.列表中第一个数字表示值,第二个数字表示个数
2.输出的也是一个压缩列表,数值相同的且连续的需要合并
3.列表长度不足的补0
给你任意两个压缩列表,输出两个列表相乘后的压缩列表
(压缩列表的解压后的个数为0-2^32之间)
a =  [2, 2, 2, 4, 4, 4, 4, 4 ]      压缩后为 [[2, 3], [4, 5]]
b = [4, 4, 4, 2, 2, 2, 2, 2, 2]     压缩后为 [[4, 3], [2, 6]]
a*b = [8, 8, 8, 8, 8, 8, 8, 8, 0]   压缩后为 [[8, 8], [0, 1]]

a = [1, 1, 2, 2, 2, 2, 2, 2, 2]     压缩后为 [[1, 2], [2, 7]]
b = [2, 2, 2, 4, 4, 4, 4, 4]        压缩后为 [[2, 3], [4, 5]]
a*b = [2, 2, 4, 8, 8, 8, 8, 8, 0]   压缩后为 [[2, 2], [4, 1], [8, 5], [0, 1]]

现有
压缩列表a = [[1, 9000000], [2, 88888888], [3, 99999999], [4, 800000000]]
压缩列表b = [[2, 20000000], [3, 88888888], [2, 19999999], [1, 100000000]]
求 a*b 的压缩列表
'''

a = [[1, 9000000], [2, 88888888], [3, 99999999], [4, 800000000]]
b = [[2, 20000000], [3, 88888888], [2, 19999999], [1, 100000000]]

a_n = len(a)
b_n = len(b)

a_org = []
b_org = []

for i in range(a_n):
    for j in range(a[i][0]):
        a_org.append(a[i][1])

for i in range(b_n):
    for j in range(b[i][0]):
        b_org.append(b[i][1])

a_org_len = len()


#c_org = a_org*b_org
c_org = []


c_len = len(c_org)
c = []
i = 0
j = 0
#c =a*b = [2, 2, 4, 8, 8, 8, 8, 8, 0]
[2, 2] [4, 1] [8, 1] [0, 1]
while i < c_len:
    if (j == 0) :  #初始化
        t = c_org[i]
        j = 1
    else :
        if(c_org[i] == t):  #若连续 相同， j+=1
            j += 1
        else:  #若不连续时，则将之前数据加入c中，且更新t、j
            c_pop = []
            c_pop.append(t)
            c_pop.append(j)
            c.append(c_pop)
            t = c_org[i]
            j = 1
    i += 1

print(c)

