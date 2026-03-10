
#P2 assignment, Group 10 with Lydia McPhee, Rebeca Oliveira, Nina Freeman and Mason Stewart

#I am creating the functions that will display the welcome message and the menu to make a choice from

#Mason Stewart - Main function/proofreading
#troubleshooting using global variables.

def main():
    player_name = introduction()   # Get player's name
    home_team = ""
    teams = ["Tigers", "Lions", "Eagles", "Sharks"]
    wins = 0
    losses = 0

    while True:
        choice = menu()  # Show menu and get choice

        if choice == 1: #Chose Teams
            home_team = choose_team(teams)
            opponent_team = choose_team(teams, remove_team=home_team)
        elif choice == 2: #Play Game; this one has some weird stuff bc of global variables to track
            result = play_game(home_team, opponent_team)
            if result == "W":
                wins = wins + 1
            else:
                losses = losses + 1
        elif choice == 3: #Display Record
            display_record(home_team, wins, losses)

        elif choice == 4: #end
            print(f"Goodbye, {player_name}!")
            break

#Nina Freeman
#introduction function
def introduction():
    #making the input grammatically correct
    name = input("What is your name? ")
    #print welcome message and rules, personalizing it with the user name
    print(f'Welcome {name} to our Soccer Season Simulator! Throughout this program you will get to pick your own home team ')
    print(f'and they will go up against various other teams of your choosing.')
    print('Scores for each game will be randomized, resulting in the higher score winning.')
    print("After playing through, you'll be able to review the scores for each game.\n")
    print('---Have fun and good luck!---')
    #return the name inputted so it can be used later on
    return name

#menu function
def menu():
    #print choices
    print('---Menu---')
    print('1 - Choose your team\n' 
    '2 - Play game\n' 
    '3 - Display Records\n' 
    '4 - Exit\n')

    #set up while loop to ensure that we get a valid input
    while True:
        choice = input('Enter your choice: ')
        #protect code
        try:
            #converting and checking the input
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice
            else:
                print('Please choose a number between 1 an 4.')
        #sending the user back to enter a choice 
        except ValueError:
            print('Invalid choice. Please try again.')

# Lydia McPhee

# Function to allow user to choose a team
# This function can be used to select both the home team and the opponent
# If a team is passed in through remove_team, that team will be removed
# so it cannot be selected again.

def choose_team(teams, remove_team=None):

    # Create a copy of the team list so the original list doesn't change
    available_teams = teams.copy()

    # If a team was passed into remove_team, remove it from the options
    if remove_team is not None and remove_team in available_teams:
        available_teams.remove(remove_team)

    print("\n---Team Selection---")

    # Display the teams as a numbered list
    for i, team in enumerate(available_teams, 1):
        print(f"{i} - {team}")

    # Loop until the user enters a valid choice
    while True:
        choice = input("Select a team by entering the number: ")

        try:
            choice = int(choice)

            if 1 <= choice <= len(available_teams):
                selected_team = available_teams[choice - 1]
                return selected_team
            else:
                print("Please choose a valid number from the list.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# Rebeca Mousser
# Women's Soccer Seasobn Game

import random

# Simulates a soccer game between the home team and opponent. 
# Generates random scores with no ties. 
# Returns "W" if home team wins and "L" if home team loses.

def play_game(home_team, away_team):
    home_score = random.randint(0, 5)
    away_score = random.randint(0, 5)

    # Ensure there are no ties
    while home_score == away_score:
        away_score = random.randint(0, 5)

    print(f"\nGame Result: ")
    print(f"{home_team}: {home_score}")
    print(f"{away_team}: {away_score}")

    if home_score > away_score:
        print(f"{home_team} wins!\n")
        return "W"
    else:
        print(f"{home_team} loses.\n")
        return "L"

    
# Display the final record for the selected team
def display_record(team_name, wins, losses):
    print(f"\nCurrent record for {team_name}: ")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print("")


#Run the Program
main()

