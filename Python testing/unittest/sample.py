def check_even(input):
    if type(input) != int:
        raise ValueError("please enter a valid input")
    else:
        if input % 2 == 0:
            return 1
        else:
            return 0
