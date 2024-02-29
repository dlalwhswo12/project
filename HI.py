import random
def up_down_game():
    best_attempt = None
    while True:
        # 게임 플레이어의 최고 시도 횟수 출력
        if best_attempt:
            print(f"이전 게임 플레이어 최대 시도: {best_attempt}")
        # 게임 시작
        secret_number = random.randint(1, 100)
        attempts = 0
        print("Up Down 게임을 시작합니다!")
        print("1부터 100 사이의 숫자를 맞춰보세요.")
        while True:
            try:
                user_guess = int(input("숫자를 입력하세요: "))
                if user_guess < 1 or user_guess > 100:
                    print("유효한 범위 내의 숫자를 입력하세요.")
                    continue
            except ValueError:
                print("유효한 숫자를 입력하세요.")
                continue
            attempts += 1
            if user_guess == secret_number:
                print("성공입니다.")
                print(f"시도한 횟수: {attempts}")
                break
            elif user_guess < secret_number:
                print("업")
            else:
                print("다운")
        # 이전 게임 플레이어의 최대 시도 경험 업데이트
        if not best_attempt or attempts > best_attempt:
            best_attempt = attempts
        # 다시 플레이할지 묻기
        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다.")
            break
if __name__ == "__main__":
    up_down_game()