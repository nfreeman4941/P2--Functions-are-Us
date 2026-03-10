#Nina Freeman

#P2 assignment, Group 10 with Lydia McPhee, Rebeca Oliveira, and Mason Stewart

#I am creating the functions that will display the welcome message and the menu to make a choice from

#introduction function
def introduction(name):
    #making the input grammatically correct
    name = name.title()
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
