# Правильная скобочная последовательность
# ("{()}[]") -> true
# ("{[}]") -> false

def paranf_check(string):
    stack = []
    dict_ = {
        ')':'(',
        '}': '{',
        ']':'['
    }
    for paran in string:
        if paran in '({[':
            stack.append(paran)
        elif stack[-1] == dict_[paran]:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    return False

print(paranf_check('{[)}'))
