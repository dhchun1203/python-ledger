print("=== 나의 가계부 ===")
 
entries = []
 
while True:
    print()
    print("1. 기록 추가")
    print("2. 목록 보기")
    print("3. 가장 큰 지출")
    print("4. 끝내기")
    choice = input("선택: ")
 
    if choice == "1": # 기록 추가
        kind = input("종류(수입/지출): ")
        while kind != "수입" and kind != "지출":
            print("수입 또는 지출로 입력해 주세요.")
            kind = input("종류(수입/지출): ")
 
        category = input("분류: ")
        item = input("항목: ")
 
        amount_text = input("금액: ")
        while not amount_text.isdigit():
            print("숫자만 입력해 주세요.")
            amount_text = input("금액: ")
        amount = int(amount_text)
 
        entry = {"kind": kind, "category": category, "item": item, "amount": amount} # 모든 입력값을 받고 객체를 만든다.
        entries.append(entry)
        print("기록했어요.")
    elif choice == "2": # 목록 보기
        balance = 0
        print(f"모두 {len(entries)}건")
        for entry in entries:
            if entry["kind"] == "수입":
                sign = "+"
                balance += entry["amount"]
            else:
                sign = "-"
                balance -= entry["amount"]
            print(f"[{entry['category']}] {entry['item']} {sign}{entry['amount']:,}원")
        print(f"잔액: {balance:,}원")
    elif choice == "3": # 가장 큰 지출
        biggest = None
        for entry in entries:
            if entry["kind"] == "지출":
                if biggest is None or entry["amount"] > biggest["amount"]:
                    biggest = entry
        if biggest is None:
            print("지출 기록이 없어요.")
        else:
            print(f"가장 큰 지출: [{biggest['category']}] {biggest['item']} -{biggest['amount']:,}원")
    elif choice == "4": # 끝내기
        print("다음에 또 만나요.")
        break
    else:
        print("메뉴 번호로 골라 주세요.")