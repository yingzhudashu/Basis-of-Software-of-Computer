# coding = utf-8
# @author:yingzhudashu

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
frequency = [0.25, 0.1, 0.12, 0.2, 0.15, 0.07, 0.11]
tree0 = []

def chose():
    tree = ['', [], []]

    m0 = min(frequency)
    m = frequency.index(m0)
    tree[1] = tree0[m]
    tree[0] = tree0[m][0]
    frequency.pop(m)
    tree0.pop(m)

    n0 = min(frequency)
    n = frequency.index(n0)
    tree[2] = tree0[n]
    tree[0] = tree[0] + tree0[n][0]
    frequency.pop(n)
    tree0.pop(n)

    frequency.append(m0+n0)
    tree0.append(tree)

def find(tree0, i):
    if i in tree0[1][0]:
        print('0', end='')
        if i == tree0[1][0]:
            return 0
        else:
            find(tree0[1], i)

    elif i in tree0[2][0]:
        print('1', end='')
        if i == tree0[2][0]:
            return 0
        else:
            find(tree0[2], i)

def main():
    for i in range(7):
        tree0.append([letters[i], [], []])
    for i in range(6):
        chose()
    print(tree0)
    for i in letters:
        print(i, end=' ')
        find(tree0[0], i)
        print('')

if __name__ == "__main__":
    main()