print("=== 나의 가계부 ===")

total_amount = 0

category = input("분류 : ")
item = input("항목: ")
amount = int(input("금액: "))
total_amount += amount

category2 = input("분류 : ")
item2 = input("항목: ")
amount2 = int(input("금액: "))
total_amount += amount2

print(f"[{category}] {item} {amount:,}원")
print(f"[{category2}] {item2} {amount2:,}원")
print(f"오늘 합계: {total_amount:,}원")
