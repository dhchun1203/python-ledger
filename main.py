def ask_kind():
    kind = input("종류(수입/지출): ")
    while kind != "수입" and kind != "지출":
        print("수입 또는 지출로 입력해 주세요.")
        kind = input("종류(수입/지출): ")
    return kind

def ask_amount():
    amount_text = input("금액: ")
    while not amount_text.isdigit():
        print("숫자만 입력해 주세요.")
        amount_text = input("금액: ")
    return int(amount_text)


def add_entry(entries):
    kind = ask_kind()
    category = input("분류: ")
    item = input("항목: ")
    amount = ask_amount()

    entry = {"kind": kind, "category": category, "item": item, "amount": amount} # 모든 입력값을 받고 객체를 만든다.
    entries.append(entry)
    print("기록했어요.")

def signed_amount(entry):
    return -entry["amount"] if entry['kind'] == "지출" else entry["amount"]

def balance(entries):
    total = 0
    for entry in entries:
        total += signed_amount(entry)
    return total

def show_list(entries):
    print(f"모두 {len(entries)}건")
    for entry in entries:
        print(f"{signed_amount(entry):>+12,}원  [{entry['category']}] {entry['item']}")
    print(f"잔액: {balance(entries):,}원")

def show_biggest(entries):
    biggest = None
    for entry in entries:
        if entry["kind"] == "지출":
            if biggest is None or entry["amount"] > biggest["amount"]:
                biggest = entry
    if biggest is None:
        print("지출 기록이 없어요.")
    else:
        print(f"가장 큰 지출: [{biggest['category']}] {biggest['item']} -{biggest['amount']:,}원")
def show_totals(entries):
    totals = {}
    for entry in entries:
        if entry["kind"] == "지출":
            category = entry["category"]
            totals[category] = totals.get(category, 0) + entry["amount"]  
    if totals:
        total_amount = sum(totals.values())
        ranked = sorted(totals.items(), key=lambda pair: pair[1], reverse=True)
        for category, total in ranked:
            ratio = (total / total_amount) * 100
            print(f"{category}: {total:,}원 ({ratio:.1f}%)")  
    else:
        print("지출 기록이 없어요.")

def main():
    print("=== 나의 가계부 ===")
    entries = []

    while True:
        print()
        print("1. 기록 추가")
        print("2. 목록 보기")
        print("3. 가장 큰 지출")
        print("4. 분류별 지출")
        print("5. 끝내기")
        choice = input("선택: ")

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            show_list(entries)
        elif choice == "3":
            show_biggest(entries)
        elif choice == "4":
            show_totals(entries)
        elif choice == "5":
            print("다음에 또 만나요.")
            break
        else:
            print("메뉴 번호로 골라 주세요.")

if __name__ == "__main__":
    main()