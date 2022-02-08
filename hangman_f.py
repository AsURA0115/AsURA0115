import random
import string

def game_banner():
    print('H A N G M A N')

def game_menu():
    game_status = True
    while game_status:
        user_response = input('Type "play" to play the game, "exit" to quit: ')
        if user_response == 'play':
            game_status = False
            return True
        elif user_response == 'exit':
            game_status = False
            return False

def input_validation(letter):
    if len(str(letter)) != 1:
        print("You should input a single letter")
        return False
    elif not str(letter) in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
        return False
    return True

def guess_word():
    word = ('python', 'java', 'kotlin', 'javascript')
    computer_choice = random.choice(word)
    guessed_word = '-' * (len(computer_choice))
    player_lives = 8
    user_inputs = list()
    while player_lives > 0:
        print()
        print("".join(guessed_word))
        user_guess = input('Input a letter: ')
        if not input_validation(user_guess):
            continue
        if user_guess in guessed_word or user_guess in user_inputs:
            print("You've already guessed this letter")
            continue
        elif user_guess in computer_choice:
            index = 0
            for _ in computer_choice:
                if computer_choice[index] == user_guess:
                    guessed_word = list(guessed_word)
                    guessed_word[index] = user_guess
                index += 1
            if '-' not in guessed_word:
                print("".join(guessed_word))
                print('You guessed the word!')
                print('You survived!')
                break
        else:
            player_lives -= 1
            print("That letter doesn't appear in the word")
            user_inputs += user_guess
            continue
    else:
        print('You lost!')

def main():
    game_banner()
    if game_menu():
        guess_word()

if __name__ == "__main__":
    main()
