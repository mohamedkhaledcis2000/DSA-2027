# --------------------
# -- Calculate Time --
# --------------------

def seconds_to_hms(seconds):

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours}:{minutes:02d}:{seconds:02d}"

# ----------------------------
# -- Temperature Conversion --
# ----------------------------

def celsius_to_fahrenheit(celsius):

    fahrenheit = celsius *9 / 5 + 32

    return round(fahrenheit, 1)

# ------------------
# -- Split Evenly --
# ------------------

def split_evenly(total, people):

    share = total // people
    left_over = total % people

    return (share, left_over)

# --------------
# -- Initials --
# --------------

def initials(full_name):

    full_name = full_name.split()

    initials_letters = [name[0].upper()+"." for name in full_name]

    return f'{"".join(initials_letters)}'

# ------------------------
# -- is_palindrome_word --
# ------------------------

def is_palindrome_word(word):

    return word.strip().lower() == word.strip().lower()[::-1]

# ----------------
# -- mask_email --
# ----------------

def mask_email(email):

    the_at_index = email.index("@")
    name = email[:the_at_index]
    domain = email[the_at_index:]

    if len(name) <= 2:

        return email
    else:

        return name[0] + "*" * (len(name) - 2) + name[-1] + domain

# ------------
# -- middle --
# ------------

def middle(values):

    if len(values) == 0:
        return []

    elif len(values) % 2 == 0:

        mid_index = len(values) // 2

        return values[mid_index - 1 : mid_index + 1]
    
    else:

        mid_index = len(values) // 2

        return [values[mid_index]]

# -----------------
# -- rotate_left --
# -----------------

def rotate_left(values, k):

    len_values = len(values)
    k = k % len_values if len_values > 0 else 0

    return values[k:] + values[:k]

# --------------------
# -- fibonacci list --
# --------------------

def fib_list(n):

    a, b = 0, 1
    fib_numbers = []

    while len(fib_numbers) < n:

        fib_numbers.append(a)

        a, b = b, a + b

    return fib_numbers

# -------------------
# -- Collatz Steps --
# -------------------

def collatz_steps(n):

    steps = 0

    if n < 1:
        raise ValueError("Input must be a positive integer greater than or equal to 1.")

    while n != 1:

        if n % 2 == 0 :

            n = n / 2
            steps += 1

        else:

            n = 3*n + 1
            steps += 1

    return steps


# seconds_to_hms Tests

print(seconds_to_hms(59))
print(seconds_to_hms(3725))
print(seconds_to_hms(86400))
print("=" * 40)

# celsius_to_fahrenheit Tests

print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-40))
print(celsius_to_fahrenheit(36.6))
print("=" * 40)

# split_evenly Tests

print(split_evenly(100, 3))
print(split_evenly(90, 3))
print(split_evenly(5, 8))
print("=" * 40)

# initials Tests

print(initials("haitham el-ghareeb"))
print(initials("  Ada   King  Lovelace "))
print(initials(""))
print("=" * 40)

# is_palindrome_word Tests

print(is_palindrome_word("Level"))
print(is_palindrome_word(" noon "))
print(is_palindrome_word("python"))
print(is_palindrome_word(""))
print("=" * 40)

# mask_email Tests

print(mask_email("haitham@example.com"))
print(mask_email("ab@x.org"))
print("=" * 40)

# middle Tests

print(middle([1, 2, 3]))
print(middle([1, 2, 3, 4]))
print(middle([]))
print("=" * 40)

# rotate_left Tests

print(rotate_left([1, 2, 3, 4, 5], 2))
print(rotate_left([1, 2, 3], 4))
print(rotate_left([], 3))
print("=" * 40)

# fib_list Tests

print(fib_list(0))
print(fib_list(1))
print(fib_list(7))
print("=" * 40)

# collatz steps Tests

print(collatz_steps(1))
print(collatz_steps(6))
print(collatz_steps(27))
