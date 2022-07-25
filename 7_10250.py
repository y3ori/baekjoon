test = int(input())

for _ in range(test) :
    h, w, n = map(int,input().split())

    floor = n % h
    room = n // h + 1

    if n % h == 0 :
        floor = h
        room = n // h
    
    print(floor * 100 + room)