import ui

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
            ui.add_entry(entries)
        elif choice == "2":
            ui.show_list(entries)
        elif choice == "3":
            ui.show_biggest(entries)
        elif choice == "4":
            ui.show_totals(entries)
        elif choice == "5":
            print("다음에 또 만나요.")
            break
        else:
            print("메뉴 번호로 골라 주세요.")

if __name__ == "__main__":
    main()