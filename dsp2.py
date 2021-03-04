import queue
import plotly.offline as of
import plotly.graph_objs as go
import numpy as np


# 平均滤波器
def avg(list1 = [], m = 0):
    q = queue.Queue()
    l = []
    for i in range(0,m):
        q.put(list1[i])
    for i in range(m - 1, len(list1)-1):
        sum = 0
        for j in range(0,m):
            num = q.get()
            sum += num
            q.put(num)
        l.append(sum/m)
        # print(sum)
        q.get()
        q.put(list1[i+1])
    sum = 0
    for j in range(0, m):
        num = q.get()
        sum += num
        q.put(num)
    l.append(sum / m)
    # print(sum)
    return l


# 中值滤波器
def mid(list1 = [], m = 0):
    q = queue.Queue()
    l = []
    for z in range(0, m):
        q.put(list1[z])

    for i in range(m - 1, len(list1)-1):
        num = 0
        temp1 = []
        for j in range(0, m):
            temp1.append(q.get())
        temp2 = sorted(temp1)
        for k in range(0, int(m/2)+1):
            num = temp2[k]
        for la in temp1:
            q.put(la)
        l.append(num)
        q.get()
        q.put(list1[i+1])
    num = 0
    temp1 = []
    for j in range(0, m):
        temp1.append(q.get())
    temp2 = sorted(temp1)
    for k in range(0, int(m / 2) + 1):
        num = temp2[k]
    for la in temp1:
        q.put(la)
    l.append(num)
    q.get()
    q.put(list1[i + 1])
    return l


x1 = []
for v in range(0,100):
    x1.append(v)
l1 = [4,5,2,7,3,0,7,9,1,5,3,8]
l2 = [np.random.random() for i in range(pow(2,10))]


a = avg(l2, 5)
print(a)

b = mid(l2, 5)
print(b)


# 原数据图
# trace0 = go.Scatter(
#     x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#     y=l1
# )
# data = go.Data([trace0])
# of.plot(data)



trace0 = go.Scatter(
    x=x1,
    y=l2
)
trace1 = go.Scatter(
    x=x1,
    y=a
)
trace2 = go.Scatter(
    x=x1,
    y=b
)
data = go.Data([trace0, trace1, trace2])
of.plot(data)

















