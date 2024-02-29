import random
def get_user_choice():
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return user_choice.lower()
def determine_winner(player, computer):
    if player == computer:
        return "무승부"
    elif (
        (player == '가위' and computer == '보') or
        (player == '바위' and computer == '가위') or
        (player == '보' and computer == '바위')
    ):
        return "플레이어 승리"
    else:
        return "컴퓨터 승리"
def print_results(player, computer, result):
    print(f"플레이어: {player}, 컴퓨터: {computer}")
    print(f"결과: {result}")
def rock_paper_scissors():
    player_wins = 0
    computer_wins = 0
    ties = 0
    while True:
        print("\n가위바위보 게임을 시작합니다.")
        player_choice = get_user_choice()
        computer_choice = random.choice(['가위', '바위', '보'])
        result = determine_winner(player_choice, computer_choice)
        print_results(player_choice, computer_choice, result)
        if result == "플레이어 승리":
            player_wins += 1
        elif result == "컴퓨터 승리":
            computer_wins += 1
        else:
            ties += 1
        print(f"\n현재 스코어 - 플레이어: {player_wins}, 컴퓨터: {computer_wins}, 무승부: {ties}")
        play_again = input("게임을 계속하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("\n게임을 종료합니다.")
            print(f"게임 통계 - 플레이어: {player_wins}, 컴퓨터: {computer_wins}, 무승부: {ties}")
            break
if __name__ == "__main__":
    rock_paper_scissors()