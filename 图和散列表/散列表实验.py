# coding = utf-8
# @author:yingzhudashu

ls = eval(input("关键字序列:"))
n = eval(input("关键字个数:"))
m = eval(input("哈希表长度:"))
p = eval(input("取余的质数:"))
sos = eval(input("解决冲突的探测法次数:"))

def H(k):
    k = k % p
    return k

def H1(HashTable, k):
    for i in range(1, m):
        d = (k + i) % m
        if HashTable[d] == 0:
            return d

def H2(HashTable, k):
    for i in range(1, m//2 + 1):
        d = (k + i * i) % m
        if HashTable[d] == 0:
            return d
        d = (k + (-i) * i) % m
        if HashTable[d] == 0:
            return d

def reseach1(HashTable, l):
    k = H(l)
    count = 0
    for i in range(k, m * 2):
        d = i % m
        count = count + 1
        if HashTable[d] == l:
            return count

def reseach2(HashTable, l):
    count = 0
    for i in range(l, p * 2):
        d = i % p
        count = count + 1
        if HashTable[d] == 0:
            return count

def main():
    #初始化哈希表
    HashTable = []
    for i in range(m):
        HashTable.append(0)

    #求出地址
    for i in range(n):
        k = H(ls[i])
        if HashTable[k] == 0:
            HashTable[k] = ls[i]
        elif sos == 1:
            d = H1(HashTable, k)
            HashTable[d] = ls[i]
        elif sos == 2:
            d = H2(HashTable, k)
            HashTable[d] = ls[i]

    #输出哈希表
    print(HashTable)

    #查找成功的ASL
    number1 = 0
    ach = []
    for i in range(n):
        ach.append(reseach1(HashTable, ls[i]))
        number1 = number1 + ach[i]
    ASL1 = 0.0
    ASL1 = number1 / n
    print(ach)
    print("查找成功的ASL:{}".format(ASL1))

    # 查找失败的ASL
    number2 = 0
    fai = []
    for i in range(p):
        fai.append(reseach2(HashTable, i))
        number2 = number2 + fai[i]
    ASL2 = 0.0
    ASL2 = number2 / n
    print(fai)
    print("查找失败的ASL:{}".format(ASL2))

if __name__ == '__main__':
    main()