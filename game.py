import random as rnd
import keyboard as kb

class Die:
    def __init__(self, sides=6):    # Initializing with default
        self.sides = sides
    def UpdateSides(self, sides):   # Allowing sides to be reset
        self.sides = sides
    def roll(self):     # Grabbing random number based on type of die
        return str(rnd.randint(1, self.sides))  # Returning as string for easier concatenation


# Global variables
play = True
total_players = 0
dice = 0
sides = 0
players = []
player_roll = ''
roll = ''
temp_roll = ''
leading_roll = '0'
die = Die()
computer = 0
winner = 0
# Formatting things to make the code look a little less CLIish
mini_break_line = (' ' * 9) + '*' + ('-' * 47) + '*'
break_line = '*----*---------*-----------------*-----------------*---------*----*'
substitute_break_line = (' ' * 5) + '*' + '-----------*---------*-----*-----*---------*-----------' + '*'
mini_pad_amount = 48
pad_amount = 66


def Main():
    global play
    global computer

    Hello()

    while play:     # Keeps the code running til the user ends it
        GetInfo()
        for i in range(total_players):
            players.append(i + 1)   # Making a list with all the players
        while len(players) != 0:    # Keeps running until all players have gone
            current_player = players[(rnd.randint(0, len(players) - 1))]    # Grabbing a random player
            if current_player == 1: # Arbitrary choice, just saying the user is the first
                PlayerRolls()
            else:
                computer = current_player - 1   # Grabbing which non user is going
                ComputerRolls()
            players.remove(current_player)  # Eliminating the player who just went

        DisplayWinner()
        Continue()
    GoodBye()


def Hello():
    # Just some friendly information for the user
    print('\n' + mini_break_line)
    print((' ' * 9) + '| Let\'s Play! '.ljust(mini_pad_amount, '-') + '|')
    print((' ' * 9) + '| How it works: each player rolls a set amount '.ljust(mini_pad_amount, '-') + '|')
    print((' ' * 9) + '| of dice, and those values are concatenated. '.ljust(mini_pad_amount, '-') + '|')
    print((' ' * 9) + '| The player with the highest number wins. '.ljust(mini_pad_amount, '-') + '|')
    print(mini_break_line)
    print()


def GetInfo():
    global total_players
    global dice
    global sides
    global die

    print('\n')
    print(substitute_break_line)

    total_players = GetInput((' ' * 10) + 'How many players do you want to play against? ') + 1
    dice = GetInput((' ' * 13) + 'How many dice do you want to play with? ')
    sides = GetInput((' ' * 11) + 'What side dice would you like to play with? ')

    print(substitute_break_line)
    print()
    die.UpdateSides(sides)


def GetInput(string):
    result = 0
    while True: # Staying until user inputs valid data
        try:
            result = int(input(string))
        except ValueError:  # Error happens if user did NOT input integer
            print("| Must input an integer.")
            continue
        break   # Breaks when input is valid
    return result


def PlayerRolls():
    global dice
    global player_roll
    global die

    print(break_line)
    GetRoll()
    print(break_line)
    print(('| Your roll was ' + player_roll + '.').ljust(pad_amount, ' ') + '|')

    winning = CompareRolls(player_roll)
    if winning:
        print('| You\'re in the lead. For now.'.ljust(pad_amount, ' ') + '|')
    else:
        print('| Your roll wasn\'t high enough. Maybe you should try not sucking.'.ljust(pad_amount, ' ') + '|')


def GetRoll():
    kb.add_hotkey('r', AddToRoll)   # Calls the AddToRoll method when user presses the 'r' key
    for i in range(dice):
        print(('| Press \'r\' to roll die #' + str(i + 1) + '. (Don\'t hit enter)').ljust(pad_amount, ' ') + '|')
        kb.wait('r')    # Halts the program until the user rolls
        kb.send('del')  # Deletes the r the user typed
    kb.unhook_all_hotkeys()     # Stops listening for keystrokes


def AddToRoll():
    global die
    global player_roll
    global temp_roll
    temp_roll = die.roll()  # Grabs random die roll
    player_roll += temp_roll    # Concatenates the user's roll to the running string
    print(('| Your roll: ' + temp_roll).ljust(pad_amount, ' ') + '|')


def ComputerRolls():
    global dice
    global roll
    global die
    global computer
    global winner

    print(break_line)
    for i in range(dice):
        roll += die.roll()  # Concatenates the computer's roll to the running string
    print(('| Computer #' + str(computer) + ' rolled ' + roll + '.').ljust(pad_amount, ' ') + '|')

    winning = CompareRolls(roll)
    if winning:
        print('| It\'s in the lead, sucka!'.ljust(pad_amount, ' ') + '|')
        winner = computer   # Saving which computer is winning
    else:
        print('| This computer sucks. Just like you.'.ljust(pad_amount, ' ') + '|')
    roll = ''


def CompareRolls(roll):
    global leading_roll
    best_roll = int(leading_roll)
    test_roll = int(roll)

    if test_roll >= best_roll:
        leading_roll = str(test_roll)
        return True
    else:
        return False


def DisplayWinner():
    global player_roll
    global leading_roll
    global winner

    print(break_line)
    if int(player_roll) >= int(leading_roll):
        print('| You won... This time...'.ljust(pad_amount, ' ') + '|')
    else:
        print(('| Yeah, you suck, homie. Computer #' + str(winner) + ' won.').ljust(pad_amount, ' ') + '|')
    print(break_line)


def Continue():
    global play
    answer = 'x'

    # print('\n')
    print()
    while answer.lower() != 'y' and answer.lower() != 'n':  # Checking for valid input
        print(substitute_break_line)
        answer = input('        Would you like to keep playing? Enter \'y\' or \'n\': ')
        print(substitute_break_line)
        print()
        ResetVariables()
    if answer == 'n':
        play = False


def ResetVariables():
    global player_roll
    global roll
    global leading_roll

    # Resetting some starting variables so
    player_roll = ''
    roll = ''
    leading_roll = '0'


def GoodBye():
    # Displaying a fairwell to the user
    print('\n\n\n')
    print('*----------------------------------------------*')
    print('| Thanks for playing! I hope you lost a bunch. |')
    print('*----------------------------------------------*'.ljust(pad_amount, '-') + '*')
    print('|                                 /\\'.ljust(pad_amount, ' ') + '|')
    print('|                      /\\        //\\\\'.ljust(pad_amount, ' ') + '|')
    print('|         PANGA       /  \\      ///\\\\\\             /\\'.ljust(pad_amount, ' ') + '|')
    print('| /\\     DEV OPS     /    \\    ////\\\\\\\\     /\\    /  \\            |')
    print('|/ /\\               /      \\  /////\\\\\\\\\\   /  \\  /    \\   /\\     /|')
    print('| / /\\        /\\   /    /\\  \\//////\\\\\\\\\\\\ / /\\ \\/     /\\ /  \\   /\\|')
    print('|/ /  \\  /\\  //\\\\ /    /  \\ ///////\\\\\\\\\\\\/ /  \\ \\    //\\\\ /\\ \\ //\\|')
    print('| / /\\ \\/  \\///\\\\\\    / /\\ \\///////\\\\\\\\\\/ / /\\ \\ \\  ///\\\\\\  \\ ///\\|')
    print('|/ /  \\ \\  ////\\\\\\\\  / /  \\ \\//////\\\\\\\\/ / /  \\ \\ \\////\\\\\\\\\\ ////\\|')
    print('| / /\\ \\ \\/////\\\\\\\\\\/ / /\\ \\ \\/////\\\\\\/ / / /\\ \\ \\/////\\\\\\\\\\/////\\|')
    print(break_line)


Main()
