# -- decisions --------------------------------------------------------------

def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle")

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


def course_result(coursework, final, attendance):

    if not (0 <= coursework <= 40):
        raise ValueError("Invalid coursework")

    if not (0 <= final <= 60):
        raise ValueError("Invalid final")

    if not (0 <= attendance <= 100):
        raise ValueError("Invalid attendance")

    if attendance < 75:
        return "barred"

    if final < 18:
        return "fail"

    if coursework + final < 60:
        return "fail"

    return "pass"


# -- loops ------------------------------------------------------------------

def fizzbuzz(n):

    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def primes_below(n):

    primes = []

    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


def first_repeated(values):

    for i in range(len(values)):
        for j in range(i):
            if values[i] == values[j]:
                return values[i]

    return None


def count_pairs(n):

    return n * (n - 1) // 2


def calculator(command):

    parts = command.split()

    try:
        match parts[0]:

            case "add":
                return int(parts[1]) + int(parts[2])

            case "mul":
                return int(parts[1]) * int(parts[2])

            case "neg":
                return -int(parts[1])

            case "sum":
                total = 0

                for num in parts[1:]:
                    total += int(num)

                return total

            case _:
                raise ValueError("Invalid command")

    except:
        raise ValueError("Invalid command")


# -- functions --------------------------------------------------------------

def parse_int(text, default=None):

    try:
        return int(text)
    except ValueError:
        return default


def stats(*numbers):

    if len(numbers) == 0:
        raise ValueError("No numbers")

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for num in numbers:

        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

        total += num

    mean = total / len(numbers)

    return (smallest, largest, mean)


def append_to(item, target=None):

    if target is None:
        target = []

    target.append(item)

    return target


def make_multiplier(k):

    def multiply(x):
        return x * k

    return multiply


def apply_n(f, x, n):

    result = x

    for _ in range(n):
        result = f(result)

    return result


# -------------------- TESTS --------------------

print(classify_triangle(3, 3, 3))
print(classify_triangle(3, 3, 5))
print(classify_triangle(3, 4, 5))

print(course_result(35, 25, 90))
print(course_result(38, 15, 100))
print(course_result(40, 60, 70))

print(fizzbuzz(5))

print(is_prime(2))
print(is_prime(9))
print(is_prime(97))

print(primes_below(10))

print(first_repeated([3, 1, 4, 1, 5, 9, 5]))

print(count_pairs(4))
print(count_pairs(10))

print(calculator("add 2 3"))
print(calculator("mul 4 5"))
print(calculator("neg 7"))
print(calculator("sum 1 2 3 4"))

print(parse_int("42"))
print(parse_int("abc", 0))

print(stats(3, 1, 2))
print(stats(5))

print(append_to(1))
print(append_to(2))
print(append_to(3, [0]))

triple = make_multiplier(3)
print(triple(5))

print(apply_n(lambda x: x * 2, 1, 10))