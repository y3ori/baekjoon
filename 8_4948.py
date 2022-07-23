def bertrand(x) :
    if x == 1 :
        return False
    else :
        for i in range(2, int(x**(1/2)+1)) :
            if x % i == 0 :
                return False
        return True

limit = list(range(2,246912))
ans_list = []

for i in limit :
    if bertrand(i) :
        ans_list.append(i)

while True :
    cnt = 0
    num = int(input())
    if num == 0 :
        break
    else :
        for i in ans_list :
            if num < i < 2*num+1 :
                cnt += 1
    print(cnt)