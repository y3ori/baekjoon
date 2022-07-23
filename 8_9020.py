def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


t = int(input())

for _ in range(t) :
    n = int(input())
    a = n // 2
    b = a

    while a > 0 :
        if is_prime(a) and is_prime(b) :
            print(a, b)
            break
        a -= 1
        b += 1