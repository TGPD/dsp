import cmath


class DspList():

    def __init__(self, i=0, L= [0, 0, 0, 0, 0, 0]):
        self.lis = L
        self.p0 = i     #零点

    # 显示
    def readList(self, i):
        "读取"
        return self.lis[i+self.p0]

    # 写入
    def writeList(self, i, num):
        "写入"
        self.lis[i+self.p0] = num

    # 删除
    def dell(self, i):
        del self.lis[i]

    # 前补零
    def more_0_front(self, i):
        "前方补0"
        for n in range(0, i):
            self.lis.insert(0, 0)

    # 后补零
    def more_0_back(self, i):
        "后方补0"
        for n in range(0, i):
            self.lis.append(0)

    # 向前平移
    def move_forward(self, i):
        "提前"
        for n in range(0, i):
            self.lis.insert(0, 0)

        le = len(self.lis)
        for n in range(0, le - i):
            self.lis[n] = self.lis[n+i]

        for n in range(le - i, le):
            self.lis[n] = 0

    # 向后平移
    def move_backward(self, i):
        "延迟"
        for n in range(0, i):
            self.lis.append(0)

        le = len(self.lis)
        n = le - i + 1
        while n > i - 1:
            self.lis[n] = self.lis[n-i]
            n -= 1

        for n in range(0,i ):
            self.lis[n] = 0

    # 翻转
    def reversed(self):
        "反转"
        self.lis.reverse()
        self.p0 = len(self.lis) - self.p0 -1

    # 拉伸
    def extrude(self, i):
        "拉伸"
        self.p0 = self.p0 * (i+1)
        n = 1
        while n < len(self.lis):
            for k in range(0, i):
                self.lis.insert(n, 0)
                n += 1
            n += 1

    # 压缩
    def reduce(self, i):
        self.p0 = self.p0 / (i + 1)
        n = 1
        while n < len(self.lis):
            for k in range(0, i):
                del self.lis[n]
            n += 1

    # 差分
    def difference(self):
        l = []
        for n in range(0, len(self.lis) - 1):
            l.append(self.lis[n+1] - self.lis[n])
        return l

    # 累加
    def sum(self):
        l = 0
        for n in range(0, len(self.lis)):
            l += self.lis[n]
        return l


# 加法
def add(la = DspList(0,L = []) , lb = DspList(0,L = [])):
    if la.p0 > lb.p0 :
        lb.more_0_front(la.p0 - lb.p0)
        la.more_0_back(la.p0 - lb.p0)
    elif la.p0 < lb.p0 :
        la.more_0_front(lb.p0 - la.p0)
        lb.more_0_back(lb.p0 - la.p0)

    if len(la.lis) > len(lb.lis):
        lb.more_0_back(len(la.lis) - len(lb.lis))
    else :
        la.more_0_back(len(lb.lis) - len(la.lis))
    lc = DspList(0,[])
    lc.p0 = la.p0

    for i in range(0, len(la.lis)-1):
        lc.lis.append(la.lis[i] + lb.lis[i])
    return lc


# 乘法
def mul(la = DspList(0,L = []) , lb = DspList(0,L = [])):
    if la.p0 > lb.p0 :
        lb.more_0_front(la.p0 - lb.p0)
        la.more_0_back(la.p0 - lb.p0)
    elif la.p0 < lb.p0 :
        la.more_0_front(lb.p0 - la.p0)
        lb.more_0_back(lb.p0 - la.p0)

    if len(la.lis) > len(lb.lis):
        lb.more_0_back(len(la.lis) - len(lb.lis))
    else:
        la.more_0_back(len(lb.lis) - len(la.lis))
    lc = DspList(0,[])
    lc.p0 = la.p0

    for i in range(0, len(la.lis)-1):
        lc.lis.append(la.lis[i] * lb.lis[i])
    return lc


# 线性卷积
def linear_convolution(la = DspList(0, L = []) , lm = DspList(0, L = [])):
    la.reversed()
    la.p0 = lm.p0 = 0
    lea = len(la.lis)
    lem = len(lm.lis)
    lm.more_0_front(len(la.lis) - 1)
    la.more_0_front(len(lm.lis) - 1)
    lm.more_0_front(len(lm.lis) - 1)
    con = []
    for i in range(0, lea + lem - 1):
        lc = mul(la, lm)
        con.append(lc.sum())
        lm.dell(0)
    return con


# 循环卷积
def cycle_convolution(la = DspList(0, L = []) , lm = DspList(0, L = []), k = 1):
    la.reversed()
    lnew = []
    lnew += la.lis
    for i in range(1, k):
        la.lis += lnew
    lem = len(lm.lis)
    la.p0 = lm.p0 = 0
    con = []
    for i in range(0, lem):
        lc = mul(la, lm)
        con.append(lc.sum())
        print(la.lis)
        print(lm.lis)
        print(lc.lis)
        print("\n")
        lm.more_0_front(1)
    return con


# 相关性
def sim(la = DspList(0, L = []) , lm = DspList(0, L = [])):
    la.p0 = lm.p0 = 0
    lea = len(la.lis)
    lem = len(lm.lis)
    lm.more_0_front(len(la.lis) - 1)
    la.more_0_front(len(lm.lis) - 1)
    lm.more_0_front(len(lm.lis) - 1)
    con = []
    for i in range(0, lea + lem - 1):
        lc = mul(la, lm)
        con.append(lc.sum())
        lm.dell(0)
    return con


# 归一
def normal_sim(la = DspList(0, L = []) , lm = DspList(0, L = [])):
    la.p0 = lm.p0 = 0
    lea = len(la.lis)
    lem = len(lm.lis)
    sum1 = 0
    for i in range(0,lea):
        sum1 += la.lis[i]*la.lis[i]
    k1 = cmath.sqrt(sum1)
    for i in range(0,lea):
        la.lis[i] /= k1

    sum2 = 0
    for i in range(0,lem):
        sum2 += lm.lis[i] * lm.lis[i]
    k2 = cmath.sqrt(sum2)
    for i in range(0,lem):
        lm.lis[i] /= k2
    print(la.lis)
    print(lm.lis)

    lm.more_0_front(len(la.lis) - 1)
    la.more_0_front(len(lm.lis) - 1)
    lm.more_0_front(len(lm.lis) - 1)
    con = []
    for i in range(0, lea + lem - 1):
        lc = mul(la, lm)
        con.append(lc.sum())
        lm.dell(0)
    return con

l1 = DspList(3, L = [1,2,3,4,5,6,7,8,9,10])
l2 = DspList(2, L = [1,2,3,4,5])

l3 = DspList(0,[3,2,1])
l4 = DspList(0,[3,4,1])
l5 = DspList(0,[1,2,3])

# print(l1.readList(3))


# l1.writeList(6, 11)
#
# print(l1.lis)

# l1.dell(8)
# print(l1.lis)

# l1.more_0_front(1)
# print(l1.lis)

# l1.more_0_back(1)
# print(l1.lis)

# l1.move_forward(1)
# print(l1.lis)

# l1.move_backward(2)
# print(l1.lis)

# l1.reversed()
# print(l1.lis)
# print(l1.p0)

# l1.extrude(1)
# print(l1.lis)

# l1.reduce(1)
# print(l1.lis)

# l3 = add(l1, l2)
# print(l3.lis)

l3 = mul(l1, l2)
print(l1.lis)
print(l2.lis)
print(l3.lis)

# a = linear_convolution(l3,l4)
# print(a)

# a = cycle_convolution(l5,l4,3)
# print(a)

# a = sim(l1,l2)
# print(a)

# a = normal_sim(l1,l2)
# print(a)