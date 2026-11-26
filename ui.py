import ledger

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

def show_list(entries):
    print(f"모두 {len(entries)}건")
    for entry in entries:
        print(f"{ledger.signed_amount(entry):>+12,}원  [{entry['category']}] {entry['item']}")
    print(f"잔액: {ledger.balance(entries):,}원")

def show_biggest(entries):
    biggest = ledger.biggest_expense(entries)
    if biggest is None:
        print("지출 기록이 없어요.")
    else:
        print(f"가장 큰 지출: [{biggest['category']}] {biggest['item']} -{biggest['amount']:,}원")

def show_totals(entries):
    totals = ledger.category_totals(entries)
    if totals:
        total_amount = sum(totals.values())
        ranked = sorted(totals.items(), key=lambda pair: pair[1], reverse=True)
        for category, total in ranked:
            ratio = (total / total_amount) * 100
            print(f"{category}: {total:,}원 ({ratio:.1f}%)")  
    else:
        print("지출 기록이 없어요.")