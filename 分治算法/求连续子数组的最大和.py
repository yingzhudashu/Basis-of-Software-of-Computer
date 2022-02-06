# coding = utf-8
# @author:yingzhudashu

import random

def make(l):
    n = []
    for i in range(l):
        a = random.randint(-50, 50)
        n.append(a)
    return n

def bianli(n, l):
    a = []
    b = []
    for i in range(l):
        for j in range(i+1, l):
            s = 0
            for k in range(i, j+1):
                s = s + n[k]
            a.append(s)
            b.append([i, j])
    m = max(a)
    l0 = a.index(m)
    print("最大和：{}".format(m))
    print("位置：{}".format(b[l0]))

def fenzhi(n, low, high):
    if low == high:
        return low, high, n[low]
    mid = (low + high) // 2
    a, b, m1 = fenzhi(n, low, mid)
    a, b, m2 = fenzhi(n, mid + 1, high)
    a1 = a-1
    b1 = b
    now_left = n[mid]
    maxleft = now_left
    for i in range(mid - 1, low - 1, -1):
        now_left = now_left + n[i]
        if now_left > maxleft:
            maxleft = now_left
            a1 = i
    a2 = a-1
    b2 = b
    now_right = n[mid + 1]
    maxright = now_right
    for j in range(mid + 2, high + 1):
        now_right = now_right + n[j]
        if now_right > maxright:
            maxright = now_right
            b2 = j
    m3 = maxleft + maxright
    result = max(m1, m2, m3)
    if result == m1:
        a = a1
    elif result == m2:
        b = b2
    elif result == m3:
        a = a1
        b = b2
    return a, b, result


def main():
    l0 = 16
    n0 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    l1 = 100
    n1 = make(l1)
    l2 = 1000
    n2 = make(l2)

    while (1):
        r1 = eval(input("退出-0  常规数组-1  100数组-2  1000数组-3："))
        if r1 == 0: break

        r2 = eval(input("遍历算法-0  分治算法-1："))

        if r1 == 1:
            if r2 == 0:
                bianli(n0, l0)
            elif r2 == 1:
                a=fenzhi(n0, 0, l0-1)
                print("最大和：{}".format(a[2]))
                print("位置：[{},{}]".format(a[0],a[1]))

        elif r1 == 2:
            if r2 == 0:
                bianli(n1, l1)
            elif r2 == 1:
                a=fenzhi(n1, 0, l1-1)
                print("最大和：{}".format(a[2]))
                print("位置：[{},{}]".format(a[0], a[1]))

        elif r1 == 3:
            if r2 == 0:
                bianli(n2, l2)
            elif r2 == 1:
                a=fenzhi(n2, 0, l2-1)
                print("最大和：{}".format(a[2]))
                print("位置：[{},{}]".format(a[0], a[1]))


if __name__ == "__main__":
    main()