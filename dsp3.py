from PIL import Image
import numpy as np
from mpmath import im
from numpy import real
from scipy.fftpack import fft, ifft, fft2, ifft2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# 1.图像
def draw():
    l = []
    for i in range(0, 487):
        l.append(i)

    plt.figure(figsize=(8, 4))  # 创建绘图对象

    plt.plot(l, rx, "b--", linewidth=1)

    plt.xlabel("实部")  # X轴标签

    plt.ylabel("下标")  # Y轴标签

    plt.title("实部")  # 图标题

    plt.show()  # 显示图

    plt.figure(figsize=(8, 4))  # 创建绘图对象

    plt.plot(l, ix, "b--", linewidth=1)

    plt.xlabel("虚部")  # X轴标签

    plt.ylabel("下标")  # Y轴标签

    plt.title("虚部")  # 图标题

    plt.show()  # 显示图

    plt.figure(figsize=(8, 4))  # 创建绘图对象

    plt.plot(l, ax, "b--", linewidth=1)

    plt.xlabel("模")  # X轴标签

    plt.ylabel("下标")  # Y轴标签

    plt.title("模")  # 图标题

    plt.show()  # 显示图

    plt.figure(figsize=(8, 4))  # 创建绘图对象

    plt.plot(l, bx, "b--", linewidth=1)

    plt.xlabel("复角")  # X轴标签

    plt.ylabel("下标")  # Y轴标签

    plt.title("复角")  # 图标题

    plt.show()  # 显示图


# 2.a 图像
def show1():
    line1 = fft(L_array[200])
    a = ifft(line1)

    l1_array = L_array
    for i1 in range(0, 200):
        l1_array[i1] = a
    im1 = Image.fromarray(l1_array)
    im1.show()

    line2 = fft(L_array[300])
    a = ifft(line2)

    l1_array = L_array
    for i2 in range(0, 300):
        l1_array[i2] = a
    im1 = Image.fromarray(l1_array)
    im1.show()

    line3 = fft(L_array[400])
    a = ifft(line3)

    l1_array = L_array
    for i3 in range(0, 400):
        l1_array[i3] = a
    im1 = Image.fromarray(l1_array)
    im1.show()


# 2.b 图像



im0 = Image.open('1.png')

# 显示
# im.show()

# 图片转数组
im_array = np.array(im0)
# print(im_array[450][0])

L = im0.convert('L')
L_array = np.array(L)
# print(L_array[0][0])


line1 = L_array[200]
line2 = L_array[300]
line3 = L_array[400]

x = fft(line1)

# print(x)

rx = np.real(x)
ix = np.imag(x)
ax = np.abs(x)
bx = np.angle(x)

# draw()

show1()

# # 高通
# l2_array = L_array
# for j in range(0,485):
#     s = fft(l2_array[j])
#     # s = l2_array[j]
#     for c in range(0,len(s)):
#         if s[c]> -1.15093286e+03-1.14131103e+03j:
#             s[c] = 0
#     # s = ifft2(l2_array[j])
#     l2_array[j] = s
# im1 = Image.fromarray(l2_array)
# im1.show()




# 低通
# l2_array = L_array
# for j in range(0,485):
#     s = fft(l2_array[j])
#     # s = l2_array[j]
#     for c in range(0,len(s)):
#         if s[c] < 0.61675873e+02-1.14131103e+03j:
#             s[c] = 0
#     # s = ifft(l2_array[j])
#     l2_array[j] = s
# im1 = Image.fromarray(l2_array)
# im1.show()


# 带通
# l2_array = L_array
# for j in range(0,485):
#     s = fft(l2_array[j])
#     # s = l2_array[j]
#     for c in range(0,len(s)):
#         if 0.61675873e+02-1.14131103e+03j > s[c] > -1.15093286e+03-1.14131103e+03j:
#             s[c] = 0
#     # s = ifft(l2_array[j])
#     l2_array[j] = s
# im1 = Image.fromarray(l2_array)
# im1.show()

# print(fft(l2_array[10]))


# bnm = [1,2,3,4,5,6,7,234,5,2,432,64,34,21,52,3,4324,253,6,43,4]
# # print(fft(bnm))
# print(ifft(bnm))