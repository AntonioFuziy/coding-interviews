a = dict(zip(range(10), range(10)))
b = dict(zip(range(5, 15), range(15, 25)))
c = {**a, **b}

result = []

def keys_with_different_value(**kwargs) -> list[int]:
    for k, v in kwargs.items():
        if k in kwargs and k != v:
            result.append(k)
    return result
print(c)
print(keys_with_different_value(c))