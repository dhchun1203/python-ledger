print("=== 나의 가계부 ===")

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
    print(f"[{category}] {item} +{amount:,}원")
else:
    print(f"[{category}] {item} -{amount:,}원")
    if amount >= 100000:
        print("큰 지출이에요. 한 번 더 생각해 봐요.")
    elif amount < 10000:
        print("소소한 지출이에요.")