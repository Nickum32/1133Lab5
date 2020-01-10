def maxVal(n, maxnum = -9999999999999999):
    if len(n) == 0:
        return maxnum
    else:
        if n[0] > maxnum:
            maxnum = n[0]
        return maxVal(n[1:], maxnum)
