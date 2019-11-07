"""
A classic text-based game. Just run the script with any python interpreter and have fun!
"""
import time, sys


def print_slow(txt, newline=True):
    """
    Prints 'txt' to screen one character at a time like in the good ol' days.
    """
    for x in txt:  # cycle through the text one character at a time
        print(x, end="", flush=True)  # print one character, no new line, flush buffer
        time.sleep(0.05)
    if newline:
        print()  # go to new line


def yes_or_no(question):
    """
    Prints 'question' to the screen and then prompts user for 'yes' or 'no' input.
    """
    answer = input(question + "(y/n): ").lower().strip()
    print()
    while not answer in ["y", "yes", "n", "no"]:
        print_slow("Y or N only, dude.")
        answer = input(question + "(y/n):").lower().strip()
        print()
    if answer[0] == "y":
        return True
    else:
        return False


if __name__ == '__main__':

    time.sleep(1)
    print_slow("What is your name? ", False)
    name = input()
    time.sleep(1)
    
    greeting = "\nHello, {}"
    comment1 = "\n...interesting..."
    comment2 = "Do you hear that noise?\n"
    
    print_slow(greeting.format(name))
    time.sleep(1)
    print_slow(comment1)
    time.sleep(2)
    print_slow(comment2)
    time.sleep(1)
    
    if yes_or_no("What say you?"):
        print_slow("Yeah, me too.    The End")
    else:
        print_slow("Guess your ears are broken.    The End")
