# Rebeca Mousser
# Women's Soccer Seasobn Game

import random


# Simulates a soccer game between the home team and opponent. 
# Generates random scores with no ties. 
# Returns "W" if home team wins and "L" if home team loses.

def play_game():
    home_score = random.randint(0, 5)
    away_score = random.randint(0, 5)


    # Ensure there are no ties by re-generating the 
    # away score if it matches the home score
    while home_score == away_score:
        away_score = random.randint(0, 5)

    print(f"\nGame Result: ")
    print(f"{home_team}: {home_score}")
    print(f"{away_team}: {away_score}")

    # Determine the winner and return the result
    # If the home team wins, return "W". If the home team loses, return "L".
    if home_score > away_score:
        print(f"{home_team} wins!")
        return "W"
    else:
        print(f"{home_team} loses.")
        return "L"
    
# Display the final record for the selected team
def display_record(team_name, wins, losses):
    print(f"\nCurrent record for {team_name}: ")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")

#Run the Program
main()