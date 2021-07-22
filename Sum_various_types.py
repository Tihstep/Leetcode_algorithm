# Сумма чисел массива
# ([1, 2, '3x']) => 6
# ([1, 2, 'x3']) => 3
# ([1, [1, 2], 2]) => 6

def suma(array, count):
    for elem in array:
        if type(elem) == int:
            count += elem
        elif type(elem) == str:
            str_count = 0
            for sym in elem:
                if sym.isdigit():
                    str_count = str_count*10 + int(sym)
                else:
                    count += str_count
                    break
        else:
            count += suma(elem, 0)
    return count


print(suma([1, [1, 2], 2], 0))
