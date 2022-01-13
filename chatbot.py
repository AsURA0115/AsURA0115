bot_name = "Aid"
bot_year = "2022"
print('Hello! My name is {}.'.format(bot_name))
print('I was created in {}.'.format(bot_year))
print('Please, remind me your name.')
name = input()
# reading a name

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
