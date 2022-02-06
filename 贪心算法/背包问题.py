# coding = utf-8
# @author:yingzhudashu

name = [1, 2, 3, 4, 5, 6, 7]
weight = [35, 30, 60, 50, 40, 10, 25]
price = [10, 40, 30, 50, 35, 40, 30]

def fraction():
    total = 150
    value = []
    value0 = 0.0

    for i in range(7):
        value0 = price[i] / weight[i]
        value.append(value0)

    while(1):
        m = value.index(max(value))
        if total >= weight[m]:
            print("每种物品的重量：{} {}".format(name[m], weight[m]))
            total = total - weight[m]
            value0 = value0 + price[m]
            value[m] = 0
        else:
            print("每种物品的重量：{} {}".format(name[m], total))
            value0 = value0 + (price[m] / weight[m]) * total
            break
    print("总价值：{}".format(value0))

def integer():
    total = 150
    value0 = 0.0

    for i in range(7):
        m = price.index(max(price))
        if total >= weight[m]:
            print("每种物品的重量：{} {}".format(name[m], weight[m]))
            total = total - weight[m]
            value0 = value0 + price[m]
            price[m] = 0
        else:
            price[m] = 0

    print("总价值：{}".format(value0))

def main():
    while(1):
        k = eval(input("请输入（0-退出 1-分数背包 2-整数背包）："))
        if k == 0:
            break
        elif k == 1:
            fraction()
        elif k == 2:
            integer()

if __name__ == "__main__":
    main()
