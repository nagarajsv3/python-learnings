from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Guess a number 0, 1, 2 : ')
    return int(guess)

def check_result(my_list, user_guess):
    if my_list[user_guess] =='O':
        print("Won!!! Correct Guess")
        print(my_list)
    else:
        print("You lost")
        print(my_list)

def play_carnival_guessing_game():
    my_list = [' ', 'O' , ' ']

    shuffled_list = shuffle_list(my_list)

    user_guess_index = user_guess()

    check_result(shuffled_list, user_guess_index)

play_carnival_guessing_game()