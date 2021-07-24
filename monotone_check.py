# Проверка массива на монотонность
# ([0, 1, 5, 9, 15]) => true
# ([0, 1, 1, 5, 9, 9, 15]) => true
# ([15, 8, 4, 2, 1]) => true
# ([0, 1, 5, 15, 4]) => false

def monotone_check(array):
    return (all([array[i]>=array[i+1] for i in range(0,len(array)-1)])) or (all([array[i]<=array[i+1] for i in range(0,len(array)-1)]))

array = [0, 1, 5, 15, 4]
print(monotone_check([0, 1, 5, 15, 4]))
