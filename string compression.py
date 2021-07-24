# Сжатие строки
# ('AAABbbbBcCCC') => 'A3Bb3BcC3'
def compr(result, char, diff):
    if diff == 1:
        result += char
    else:
        result+= char + str(diff)
    return result
def string_compression(string):
    result = ''
    left = 0
    right = 1
    while(left < len(string)):
        while(right < len(string) and string[left] == string[right]):
            right+=1
        result = compr(result, string[left], right - left)
        left, right = right, right + 1
    return result
