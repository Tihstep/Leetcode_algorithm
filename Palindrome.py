#Палиндром
# ("Ш4л4ш") => true
#  ("Eva, can I see bees in a cave?") => true
#  ("Яндекс") => false

def palindrome(string):
    string = string.lower().replace(',',' ').replace('?',' ').split()
    l = 0
    r = len(string) - 1
    while(l < r):
        if(string[l] != string[r]):
            return False
        r -= 1
        l += 1
    return True
