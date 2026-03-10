#Mason Stewart
#The Purpose of this function is to call upon the other functions to organize the game

def main():
    player_name = introduction()
    wins = 0
    losses = 0
    home_team = ""
    while True:
        choice = menu()
        if choice == "1":
            home_team = choose_team()
            opponent_team = choose_team(home_team)
            result = play_game(home_team, opponent_team)
            if result == "W":
                wins += 1
            else:
                losses += 1
        elif choice == "2":
            display_record(home_team, wins, losses)
        elif choice == "3":
            print("Goodbye", player_name)
            break
        else:
            print("Invalid choice. Please try again.")
main()