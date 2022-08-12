class soldouterror(Exception):
    pass


chicken = 10
waiting = 1

while True:
    try:
        print("[남은치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문 하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")

        elif order <= 0:
            raise ValueError

        else:
            print("[대기번호 {0}] {1} 마리 주문 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise soldouterror

    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except soldouterror:
        print("재고소진")
        break
