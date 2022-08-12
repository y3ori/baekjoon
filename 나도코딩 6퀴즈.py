from random import *

cnt = 0

for i in range(1, 51):
    time = randint(5, 50)
    if time <= 15:
        print("[O] %d번째 손님 (소요시간 : %d분)" % (i, time))
        cnt += 1
    else:
        print("[ ] %d번째 손님 (소요시간 : %d분)" % (i, time))

print("총 탑승 승객 : %d분" % (cnt))
