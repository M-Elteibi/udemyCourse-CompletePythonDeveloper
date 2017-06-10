import random

# magic_numbers = [3, 9]
# user_number = int(input("Pick a number:"))
#
# if user_number in magic_numbers:
#     print("Congrats, You got it Right!!")
# else:
#     print("Sorry, You got it wrong!!")

def askUserandCheckNumber():
    userNumber = int(input("Please Enter your guess: between 0 and 9: "))
    if userNumber in magic_numbers:
        print("You got the number right!!")
    else:
        print("You didn't quite get it.")


magic_numbers = [random.randint(0,9) for x in range(2)]
print(magic_numbers)

chances = 3

def runProgramXTimes():
    for attempt in range(chances):
        print("This is your {} attempt.".format(attempt+1))
        askUserandCheckNumber()

runProgramXTimes()

# randomRangeLower = 0
# randomRangeUpper = 100
#
# minNum = randomRangeUpper
#
# for attempt in range(10):
#     randomNum = random.randint(randomRangeLower, randomRangeUpper)
#     print("{0} random number is {1}".format(attempt, randomNum))
#     if randomNum < minNum:
#         minNum = randomNum
#
# print(minNum)
