# Fizzbuzz is game that is played as follow:
# You have a range of numbers e.g. 1 to 100
# the game is to say, or in our case print, numbers and replace
# multiples of three with Fizz
# multiples of five with Buzz
# multiples of both three, and five with Fizzbuzz

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("Fizzbuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
