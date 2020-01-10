def reverseString(n):
    if len(n) < 1:
        return ''
    else:
        return n[-1] + reverseString(n[:-1])
    
