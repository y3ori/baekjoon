test = int(input())

for _ in range(test) :
    floor = int(input()) #층
    num = int(input()) #호
    people = [i for i in range(1, num+1)]

    for x in range(floor) :
        for y in range(1, num) :
            people[y] += people[y-1]

    print(people[-1])