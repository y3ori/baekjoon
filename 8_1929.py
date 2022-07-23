def is_prime_number(x) :
    if x == 1 :
        return False
    else :
        for i in range(2, int(x**(1/2)+1)) :
            if x % i == 0 :
                return False
        return True

m, n = map(int,input().split())

for i in range(m, n+1) :
    if is_prime_number(i) :
        print(i)