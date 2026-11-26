# signed_amount(entry), balance(entries): 4절에서 만든 그대로 옮겨요.
# biggest_expense(entries) (새로): 지출 중 금액이 가장 큰 기록 딕셔너리를 돌려줘요. 지출이 없으면 None이에요.
# category_totals(entries) (새로): 지출만 분류별로 더한 딕셔너리를 돌려줘요. 예: {"식비": 24000, "교통": 1500}. 지출이 없으면 빈 딕셔너리 {}예요.

def signed_amount(entry):
    return -entry["amount"] if entry['kind'] == "지출" else entry["amount"]

def balance(entries):
    total = 0
    for entry in entries:
        total += signed_amount(entry)
    return total

def biggest_expense(entries):
    # 지출 중 금액이 가장 큰 기록 딕셔너리를 리턴한다.
    biggest = None
    for entry in entries:
        if entry["kind"] == "지출":
            if biggest is None or entry["amount"] > biggest["amount"]:
                biggest = entry

    return biggest if len(biggest) > 0 else None

def category_totals(entries):
    # 지출만 분류별로 더한 딕셔너리를 돌려준다.
    # 예) {"식비": 24000, "교통": 1500}. 지출이 없으면 빈 딕셔너리를 리턴한다.
    totals = {}
    for entry in entries:
        if entry["kind"] == "지출":
            category = entry["category"]
            totals[category] = totals.get(category, 0) + entry["amount"]  
    return totals