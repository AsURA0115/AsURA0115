bot_name = "Aid"
bot_year = "2022"
print('Hello! My name is {}.'.format(bot_name))
print('I was created in {}.'.format(bot_year))
print('Please, remind me your name.')
name = input()  # reading a name

print('What a great name you have, {}!'.format(name))
print('Let me guess your age.')

print('Enter remaindes of dividing your age by 3.')
rem3 = abs(int(input())) % 3
print('Enter remaindes of dividing your age by 5.')
rem5 = abs(int(input())) % 5
print('Enter remaindes of dividing your age by 7.')
rem7 = abs(int(input())) % 7
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print('Your age is {}; thats a good time to start programming!'.format(age))

print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
number = int(input())
x = -1
while x != number:
    x += 1
    print(x, '!')

print('Completed, have a nice day!')

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    options1 = ["1. To repeat a statement multiple times.", "2. To decompose a program into several small subroutines."]
    options2 = ["3. To determine the execution time of a program.", "4. To interrupt the execution of a program."]
    
    print(options1[0])
    print(options1[1])
    print(options2[0])
    print(options2[1])

    answer = int(input())
    while answer != 2:
        if answer == 2:
            print('Completed, you are awesome, have a nice day!')
        else:
            print("Please, try again")
            answer = int(input())


def end():
    print('Congratulations, have a nice day!')

test()
end()

