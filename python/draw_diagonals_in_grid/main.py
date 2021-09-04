from collections import defaultdict as dd
import time

size = 9

canLine = []
listLine = {}
countLine = {}
nextLine = dd(list)

def solve():
    init()
    ans = 0
    dp = [[0 for _ in range(3**size)] for _ in range(size + 1)]
    for l in range(size):
        for i in canLine:
            for j in nextLine[i]:
                dp[l + 1][j] = max(dp[l + 1][j], dp[l][i] + countLine[j])
                ans = max(ans, dp[l + 1][j])
    return ans

def checkLine(t):
    iList = []
    cnt = 0
    for k in range(size):
        cur = t % 3
        if cur > 0:
            cnt += 1
        t //= 3
        if k > 0 and cur + iList[k - 1] == 3:
            return False, [], 0
        iList.append(cur)
    return True, iList, cnt

def canNext(i, j):
    iList = listLine[i]
    jList = listLine[j]
    for k in range(size):
        if k > 0 and jList[k] == 1 and iList[k - 1] == 1:
            return False
        if jList[k] + iList[k] == 3:
            return False
        if k < size - 1 and jList[k] == 2 and iList[k + 1] == 2:
            return False
    return True

def init():
    for i in range(3**size):
        ok, l, cnt = checkLine(i)
        if ok:
            canLine.append(i)
            listLine[i] = l
            countLine[i] = cnt
    for i in canLine:
        for j in canLine:
            if canNext(i, j):
                nextLine[i].append(j)

if __name__ == '__main__':
    print("start", time.time())
    print(solve())
    print("finish", time.time())
