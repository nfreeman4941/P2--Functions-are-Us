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