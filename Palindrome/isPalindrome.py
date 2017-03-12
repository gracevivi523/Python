s = input("input:")

def is_palindrome(s):
    len = str(s).__len__()
    for index in range(len/2):
        if s[index] == s[len-index-1]:
            continue
        else:
            print "this is not palindrome"
            break
    if index == len/2-1:
        print s+", is palindrome"
    
        
is_palindrome(s)
