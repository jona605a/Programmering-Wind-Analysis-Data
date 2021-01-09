def inputNumber(prompt):
# INPUTNUMBER Prompts user to input a number
#
# Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
# number. Repeats until user inputs a valid number.
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

def get_int_in_range(prompt, MIN, MAX):
    while True:
        # get input
        try:
            input_int = int(input(prompt))
            if MIN <= input_int <= MAX:
                return input_int
            else:
                raise Exception
        # handle errors
        except ValueError:
            print("Not an integer. Please try again.")
        except:
            print("Not within range. Please try again.")