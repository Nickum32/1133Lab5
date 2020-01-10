def reverseString(n):
    if len(n) < 1:
        return ''
    else:
        return n[-1] + reverseString(n[:-1])
def ispalindrome(string):
    
    string=string.lower()
    stored=string
    string=reverseString(string)
    if string == stored:
        print('palindrome')
    else:
        print('non-palindrome')
def mainFunction():
    keepgoing= True
    while keepgoing:
        string=input('what would you like to check?')
        ispalindrome(string)
        user_choice= input('Would you like to play again? enter "Y" or "y".')
        if user_choice == "Y" or user_choice == 'y':
            keepgoing= True
        else:
            keepgoing= False
            
