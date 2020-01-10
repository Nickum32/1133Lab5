# greatest common divisor
def GCD(a, b):
    if b>a:
        print('Error, try again')
    if a>b:
        if a % b == 0:
            return b
        else:
            remainder = a % b
            return GCD(b,remainder)
