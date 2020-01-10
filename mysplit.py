# strip
def mysplit(stringarg, delimiter):
    splitlist = []
    while True:
        if delimiter in stringarg:
            index = stringarg.find(delimiter)
            splitlist.append(stringarg[:index])
            stringarg = stringarg[index+1:]
        else:
            splitlist.append(stringarg)
            break
    
    return splitlist 
