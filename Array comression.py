# Сжатие целочисленного массива
# ([3, 2, 1, 5, 6, -1, 10]) -> '-1, 1-3, 5-6, 10'
def to_string(left, right):
    if left == right:
        return str(left)
    return str(left) + '-' + str(right)


def compression(list_):
    list_ = sorted(list_) + [None]
    l, r = 0, 1
    result = []
    while l < len(list_) - 1:
        while r < len(list_) - 1 and list_[r] - list_[l] == r - l:
            r += 1
        result.append(to_string(list_[l],list_[r-1]))
        l, r = r, r + 1
    return ', '.join(result)
