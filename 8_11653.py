def factorization(x) :
    i = 2
    while i <= x : 
        if x % i == 0 :
            print(i)
            x = x / i
        else :
            i += 1

n = int(input())

factorization(n)