first_num = int(input())
second_num = int(input())

prime_number = []

for i in range(first_num, second_num+1) :
    error = 0
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                error += 1
                break
        if error == 0 :    
            prime_number.append(i)

if len(prime_number) > 0 :
    print(sum(prime_number))
    print(min(prime_number))

else :
    print(-1)