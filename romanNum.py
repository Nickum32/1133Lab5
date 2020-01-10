#ROMAN NUMERAL CALCULATOR
def romanNum(string):
    sumRom=0
    romanDict={I:1, V:5, X:10, L:50, C:100, D:500, M:1000}
    for i in range(len(string)-1):
        if romanDict[string[i]] >= romanDict[string[i+1]]:
            sumRom +=romanDict[string[i]]
        if romanDict[string[i]] < romanDict[string[i+1]]:
            sumRom -= romanDict[string[i]]
    sumRom += romanDict[string[-1]]
            
