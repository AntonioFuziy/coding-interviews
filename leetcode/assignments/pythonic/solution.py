def print_indices_and_elements(elements) -> None:
    for index, element in enumerate(elements):
        print(index, element)


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [i for i in range(start, end+1) if i % 2 == 0]


def get_char_set_from(s: str) -> set[str]:
    return {element for element in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {k: k**(1/2) for k in range(start, end+1) if k**(1/2) % 1 == 0}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [i for i in numbers if i % 2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if (n % 2 == 0) else -1

def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [n if (n % 2 == 0) else -1 for n in numbers if (n % 5 == 0)]

def str_lengths(strings: list[str]) -> list[int]:
    return [len(string) for string in strings]


def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>"


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return 'apenascscscscscscscscscscs'


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        # You can add more code here if you need
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a >= len(self.elements):
            raise StopIteration()
        x = self.a
        self.a += 2
        return self.elements[x]

def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return (e1 + e2 + sum(others)) / (2 + len(others))


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c = {**a, **b}
    d = {**b, **a}
    result = []
    for k in c:
        if c[k] != d[k]:
            result.append(k)
    return result


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # You should add code here and remove the break
        x, y = numbers[0], numbers[-1]
        print(x, y)
        numbers = numbers[1:-1]
    if numbers:
        # You should add code here
        print(numbers[0])


def append_range(start: int, end: int, step: int=1, to: list[int]=None):
    # You may add code here
    if to is None:
      to = []
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None
