n = int(input())

data = list(map(int,input().split()))

prime_number = 0

for i in data :
    for j in range(2, i+1) :
        if i % j == 0 :
            if i == j :
                prime_number +=1 
            break

print(prime_number)