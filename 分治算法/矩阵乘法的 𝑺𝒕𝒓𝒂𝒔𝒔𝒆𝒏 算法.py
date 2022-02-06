# coding = utf-8
# @author:yingzhudashu

import numpy as np
import math

num_addorsub=0
num_mul=0
num_assign=0

def add(A, B):
    rows = len(A)
    columns = len(A[0])
    C = [list() for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            temp = A[i][j] + B[i][j]
            global num_addorsub, num_assign
            num_addorsub=num_addorsub+1
            num_assign = num_assign+1
            C[i].append(temp)
    return C

def minus(A, B):
    rows = len(A)
    columns = len(A[0])
    C = [list() for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            temp = A[i][j] - B[i][j]
            global num_addorsub,num_assign
            num_addorsub = num_addorsub + 1
            num_assign=num_assign+1
            C[i].append(temp)
    return C

def divide(A, row, column):
    length = len(A)
    B = [list() for i in range(length // 2)]
    k = 0
    for i in range((row - 1) * length // 2, row * length // 2):
        for j in range((column - 1) * length // 2, column * length // 2):
            temp = A[i][j]
            B[k].append(temp)
        k += 1
    return B

def merge(matrix_11, matrix_12, matrix_21, matrix_22):
    length = len(matrix_11)
    matrix_all = [list() for i in range(length * 2)]
    for i in range(length):
        matrix_all[i] = matrix_11[i] + matrix_12[i]
    for j in range(length):
        matrix_all[length + j] = matrix_21[j] + matrix_22[j]
    return matrix_all

def strassen(A, B):
    rows = len(A)
    if rows == 1:
        matrix_all = [list() for i in range(rows)]
        matrix_all[0].append(A[0][0] * B[0][0])
    elif(rows % 2 ==1):
        matrix_a_np = np.array(A)
        matrix_b_np = np.array(B)
        matrix_all = np.dot(matrix_a_np,matrix_b_np)
        global num_mul,num_addorsub
        num_mul = num_mul + 27
        num_addorsub=num_addorsub + 18
    else:
        s1 = minus((divide(B, 1, 2)), (divide(B, 2, 2)))
        s2 = add((divide(A, 1, 1)), (divide(A, 1, 2)))
        s3 = add((divide(A, 2, 1)), (divide(A, 2, 2)))
        s4 = minus((divide(B, 2, 1)), (divide(B, 1, 1)))
        s5 = add((divide(A, 1, 1)), (divide(A, 2, 2)))
        s6 = add((divide(B, 1, 1)), (divide(B, 2, 2)))
        s7 = minus((divide(A, 1, 2)), (divide(A, 2, 2)))
        s8 = add((divide(B, 2, 1)), (divide(B, 2, 2)))
        s9 = minus((divide(A, 1, 1)), (divide(A, 2, 1)))
        s10 = add((divide(B, 1, 1)), (divide(B, 1, 2)))
        p1 = strassen(divide(A, 1, 1), s1)
        p2 = strassen(s2, divide(B, 2, 2))
        p3 = strassen(s3, divide(B, 1, 1))
        p4 = strassen(divide(A, 2, 2), s4)
        p5 = strassen(s5, s6)
        p6 = strassen(s7, s8)
        p7 = strassen(s9, s10)
        c11 = add(add(p5, p4), minus(p6, p2))
        c12 = add(p1, p2)
        c21 = add(p3, p4)
        c22 = minus(add(p5, p1), add(p3, p7))
        matrix_all = merge(c11, c12, c21, c22)
        global num_assign
        num_assign =num_assign+22
    return matrix_all

def main():
    while (1):

        n = eval(input("退出-0 不重新生成-1 n维数组-n："))
        if n == 0: break
        elif n > 1:
            A = np.random.randint(-50, 50, size=[n, n])
            B = np.random.randint(-50, 50, size=[n, n])

        C = []
        row = len(A)
        r = eval(input("朴素矩阵算法-1   𝑆𝑡𝑟𝑎𝑠𝑠𝑒𝑛算法-2："))

        if r == 1:
            for i in range(row):
                C.append([])
                for j in range(row):
                    s = 0
                    for k in range(row):
                        s = s + A[i][k] * B[k][j]
                    C[i].append(s)
            print(C)

        elif r == 2:
            C = strassen(A, B)
            print(C)

if __name__ == "__main__":
    main()