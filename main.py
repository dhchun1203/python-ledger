print("=== 나의 가계부 ===")

kind = input("종류(수입/지출) : ")
category = input("분류 : ")
item = input("항목 : ")
amount = int(input("금액 : "))

if kind == "수입" :
    print(f"[{category}] {item} +{amount:,}")
else:
    print(f"[{category}] {item} -{amount:,}")