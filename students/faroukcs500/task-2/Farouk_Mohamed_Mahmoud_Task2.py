# -----------------------
# -- Classify Triangle --
# -----------------------

def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Violates triangle inequality")

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"


# -------------------
# -- Course Result --
# -------------------

def course_result(coursework, final, attendance):
    if not (0 <= coursework <= 40):
        raise ValueError("Coursework must be between 0 and 40")
    if not (0 <= final <= 60):
        raise ValueError("Final must be between 0 and 60")
    if not (0 <= attendance <= 100):
        raise ValueError("Attendance must be between 0 and 100")
    
    if attendance < 75:
        return "barred"
    if final < 18:
        return "fail"
    if coursework + final < 60:
        return "fail"
    return "pass"

# ---------------
# -- Fizz Buzz --
# ---------------

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# --------------
# -- Is Prime --
# --------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ------------------
# -- Primes Below --
# ------------------

def primes_below(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

# --------------------
# -- First Repeated --
# --------------------

def first_repeated(values):

    seen = []
    for val in values:
        if val in seen:
            return val
        seen.append(val)

    return None

# -----------------
# -- Count Pairs --
# -----------------

def count_pairs(n):
    return n * (n - 1) // 2

# ----------------
# -- Calculator --
# ----------------

def calculator(command):
    parts = command.split()
    if not parts:
        raise ValueError("Empty command")
    
    op = parts[0]
    match op:
        case "add" if len(parts) == 3:
            return int(parts[1]) + int(parts[2])
        case "mul" if len(parts) == 3:
            return int(parts[1]) * int(parts[2])
        case "neg" if len(parts) == 2:
            return -int(parts[1])
        case "sum" if len(parts) > 1:
            total = 0
            for p in parts[1:]:
                total += int(p)
            return total
        case _:
            raise ValueError("Invalid command or arguments")


# ---------------
# -- Parse Int --
# ---------------

def parse_int(text, default=None):
    try:
        return int(text)
    
    except (ValueError, TypeError):
        return default

# -----------
# -- Stats --
# -----------

def stats(*numbers):
    if not numbers:
        raise ValueError("No numbers provided")
    
    smallest = numbers[0]
    largest = numbers[0]
    total = 0
    count = 0
    
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num
        count += 1
        
    mean = total / count
    return (smallest, largest, mean)

# ---------------
# -- Append To --
# ---------------

def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

# ---------------------
# -- Make Multiplier --
# ---------------------

def make_multiplier(k):
    def multiplier(x):
        return x * k
    return multiplier

# -------------
# -- Apply N --
# -------------

def apply_n(f, x, n):
    current = x
    for _ in range(n):
        current = f(current)
    return current

# =======================



# -----------------------
# -- Classify Triangle --
# -----------------------

print(classify_triangle(3, 3, 3))
print(classify_triangle(3, 3, 5))
print(classify_triangle(3, 4, 5))
# print(classify_triangle(1, 2, 3))  # ValueError("Violates triangle inequality")
print("=" * 40)

# -------------------
# -- Course Result --
# -------------------

print(course_result(35, 25, 90))
print(course_result(38, 15, 100))
print(course_result(40, 60, 70))
print("=" * 40)

# ---------------
# -- Fizz Buzz --
# ---------------

print(fizzbuzz(5))
print(fizzbuzz(0))
print("=" * 40)

# --------------
# -- Is Prime --
# --------------

print(is_prime(2))
print(is_prime(9))
print(is_prime(97))
print("=" * 40)

# ------------------
# -- Primes Below --
# ------------------

print(primes_below(10))
print(primes_below(2))
print("=" * 40)

# -----------------
# -- Count Pairs --
# -----------------

print(count_pairs(4))
print(count_pairs(10))
print("=" * 40)

# ----------------
# -- Calculator --
# ----------------

print(calculator("add 2 3"))
print(calculator("neg 7"))
print(calculator("sum 1 2 3 4"))
# print("div 1 2")   # ValueError
print("=" * 40)

# ---------------
# -- Parse Int --
# ---------------

print(parse_int("42"))
print(parse_int("-7"))
print(parse_int("4.5"))
print(parse_int("abc", 0))
print("=" * 40)

# -----------
# -- Stats --
# -----------

print(stats(3, 1, 2))
print(stats(5))
# print(stats())  # ValueError
print("=" * 40)

# ---------------
# -- Append To --
# ---------------

print(append_to(1))
print(append_to(2))
print(append_to(3, [0]))
print("=" * 40)

# ---------------------
# -- Make Multiplier --
# ---------------------

triple = make_multiplier(3)
print(triple(5))
print("=" * 40)

# -------------
# -- Apply N --
# -------------

print(apply_n(lambda v:v * 2, 1, 10))
print(apply_n(str.upper, "hi", 0))