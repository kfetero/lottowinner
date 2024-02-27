import random
import os

# THIS IS JUST A SIMPLE GAME

count_games = 0 # this is the counter of games per option game
opt = 0 # it is the number of the game I choose to play
max_number = 0 # it is the biggest number in the game
loop_number = 0 #it is the quantity of numbers I have to get per game
ngames = 1 # this is the minimum of games I will play per option game
game_name =''

def clean_screen_cmd():
    os.system('cmd /c "cls"')


def main_menu():

    print("\nHola obten tus numeros ganadores aqui")
    print("Your options are")
    print("1. Lotto")
    print("2. Ozlotto")
    print("3. Powerball")
    print("4. Set for Lifee")


def set_game():
    op = int(input("Please enter the Game Option:  "))
    return op


def set_parameters(option_number):
    global max_number, loop_number, ngames, game_name
    if option_number == 1:
        # this is lotto or powerball
        #if option_number == 1:
        game_name = 'LOTTO'
        max_number = 45 # LOTTO GAME
        loop_number = 6 
        ngames = 4
        #else:
        #    max_number = 35  # powerball Game
        #    loop_number = 7
        #   ngames = 2 
    else:
        if option_number == 3:
            game_name = 'POWERBALL'
            max_number = 35
            ngames = 2 
        elif option_number == 4:
            game_name = 'SET FOR LIFE'
            max_number = 44 # this is for set for life game 
        else:
            game_name = 'OZLOTTO'
            max_number = 45  # this is for Ozlotto game
        loop_number = 7 #in this case loop_number is the same for both games
        # ngames = 1


def get_wining_numbers(loop_number, max_number):
    count = 0
    winning_numbers = []
    while count < loop_number:
        number = random.randint(1, max_number)
        if number in winning_numbers:
            count -= 1
        else:
            winning_numbers.append(number)
        count += 1
    return winning_numbers


def get_powerball_number():
    powerball_number = random.randint(1, 20)
    return powerball_number


clean_screen_cmd()
main_menu()
while opt < 1 or opt > 4:
    opt = set_game()

set_parameters(opt)
while count_games < ngames:
    print("\n " + game_name + " Wining numbers Game #  " + str(count_games + 1) + ':')
    print(str(get_wining_numbers(loop_number, max_number)))

    if opt == 3:
        print('This is powerball winner : ' + str(get_powerball_number()))

    count_games += 1
