# coding = utf-8
# @author:yingzhudashu

import random
import matplotlib.pyplot as plt

def plot(x, y, s):
    fig = plt.figure(dpi=128,figsize=(12,8))
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y, s, c='k', marker='.')
    plt.show()

def main():
    f1 = open("degreeDistribution.txt", "r")
    f2 = open("cluster.txt", "r")
    degreeDistribution = [[], []]
    cluster = [[], []]

    for line in f1:
        wordlist = line.split()
        degreeDistribution[0].append(wordlist[0])
        degreeDistribution[1].append(wordlist[1])

    for line in f2:
        wordlist = line.split()
        cluster[0].append(wordlist[0])
        cluster[1].append(wordlist[1])

    f1.close()
    f2.close()
    plot(degreeDistribution[0], degreeDistribution[1], 10)
    plot(cluster[0], cluster[1], 5)

if __name__ == '__main__':
    main()