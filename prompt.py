def prompt_yes_no(question: str)-> True | False:
    while True:
        options = (("Y", "YES"), ("N", "NO"))
        response = input(question + "(Y/N) ").strip().upper()

        if response in options[0]:
            return True
        if response in options[1]:
            return False
        else:
            print("Invalid input, please enter 'Y(es)' or 'N(o)'.")


def prompt_unit_system()-> True | False:
    while True:
        if prompt_yes_no("Would you like to use metric syste?"):
            print("You selected metric system.")
            return True
        elif prompt_yes_no("Would you like to use imperial system?"):
            print("You selected imperial system.")
            return False


def prompt_weight_height()-> tuple:
    while True:
        try:
            weight = float(input("Weight in Kg: "))
            height = float(input("Height in metres: "))
            return (weight, height)
        except ValueError:
            continue


def prompt_lb_ft_inch()-> tuple[float, float, float]:
    while True:
        try:
            pounds = float(input("Weight in pounds: "))
            break
        except ValueError:
            print("Please enter valid number for weight in pounds.")

    while True:
        try:
            feet = int(input("Height in feet: "))
            break
        except ValueError:
            print("Please enter valid number for height in feet.")

    while True:
        try:
            inches = int(input("Height in inches: "))
            break
        except ValueError:
            print("Please enter valid number for height in inches.")

    return (pounds, feet, inches)

