print("=== 나의 가계부 ===")

lines = []
amounts = []

while True:
    print()
    print("1. 기록 추가")
    print("2. 목록 보기")
    print("3. 가장 큰 지출")
    print("4. 끝내기")

    choice = input("선택 : ")
    if choice == "1":
        kind = input("종류(수입/지출) : ")
        while (kind != "수입" and kind != "지출"):
            print("수입 또는 지출로 입력해 주세요.")
            kind = input("종류(수입/지출) : ")

        category = input("분류 : ")
        item = input("항목 : ")

        amount = input("금액 : ")
        while not amount.isdigit():
            print("숫자만 입력해주세요.")
            amount = input("금액 : ")
        amount = int(amount)

        if kind == "수입" :
            lines.append(f"[{category}] {item} +{amount:,}원")
            amounts.append(amount)
        else:
            lines.append(f"[{category}] {item} -{amount:,}원")
            amounts.append(-amount)
        print("기록했어요")
    elif choice == "2":
      print(f"모두 {len(lines)}건")
      for line in lines:
        print(line)
      print(f"잔액: {sum(amounts):,}원")
    elif choice == "3":
        if len(amounts) == 0:
            print("지출 기록이 없어요.")
        elif min(amounts) < 0:
            print(f"가장 큰 지출 : {lines[amounts.index(min(amounts))]}")
        else:
            print("지출 기록이 없어요.")
    elif choice == "4":
        print("다음에 또 만나요.")
        break
    else:
        print("메뉴 번호로 골라 주세요.")