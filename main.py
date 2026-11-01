print("=== 나의 가계부 ===")

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