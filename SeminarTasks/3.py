import math

def sum_of_divisors(n):
    div_sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div_sum += i
            if i != n // i:
                div_sum += n // i
    return div_sum

def find_friendly_numbers(k):
    friendly_pairs = []
    for n in range(2, k+1):
        m = sum_of_divisors(n)
        if m <= k and n != m and sum_of_divisors(m) == n:
            if (m, n) not in friendly_pairs:
                friendly_pairs.append((n, m))
    for pair in friendly_pairs:
        print(f"{pair[0]} {pair[1]}")

k = int(input("Введите число k: "))

find_friendly_numbers(k)
