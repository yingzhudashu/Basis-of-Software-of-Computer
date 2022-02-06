# coding = utf-8
# @author:yingzhudashu

def main():
    v = [0, 10, 40, 30, 50, 35, 40, 30]
    w = [0, 35, 30, 60, 50, 40, 10, 25]
    m = [[], [], [], [], [], [], [], []]
    n = [[], [], [], [], [], [], [], []]

    for i in range(8):
        for j in range(151):
            m[i].append(0)
            n[i].append([])

    for i in range(1, 8):
        for j in range(1, 151):
            if j >= w[i] and m[i-1][j] < m[i-1][j-w[i]]+v[i]:
                m[i][j] = m[i-1][j-w[i]]+v[i]
                n[i][j] = n[i-1][j-w[i]].copy()
                n[i][j].append(i)
            else:
                m[i][j] = m[i-1][j]
                n[i][j] = n[i-1][j]

    print("装进背包物品的编号：{}".format(n[7][150]))
    print("总价值：{}".format(m[7][150]))


if __name__ == "__main__":
    main()