# letter count
def letterCount(n, count = 0):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHHIJKLMNOPQRSTUVWXYZ'
    if len(n) == 0:
        return count
    else:
        if n[0] in letters:
            count +=1
        return letterCount(n[1:], count)
