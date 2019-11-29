import random

city = ("Warsaw", "Paris", "London", "Rome")
attempt = 6   # lista prób
new_lottery = []
lottery = ""
#  losowanie  miasta


def draw(city):
    global lottery
    lottery = random.choice(city)  
    lottery = lottery.lower()
    start = input("Wellcome to my first game : CHOOSE A CITIY and and find the letter. Click ENTER and play")

    print("Wylosowane miasto to:", len(lottery) * '_ ')
    dush = len(lottery) * '_ '


def get_letter():
    global new_lottery
    guess_1 = input("Guess:")
    new_lottery.append(guess_1)
    return guess_1


def won():
    won = True
    for letter in lottery:
        if letter not in new_lottery:
            won = False
            break
    return won


def main_menu():
    global attempt
    draw(city)
    while not won() and attempt > 0:
        letter = get_letter()

        if letter not in list(lottery):
            attempt -= 1
        
        if won():
            print('you won')
            print("Wylosowane miasto to:", lottery.upper())
            break
    if attempt == 0:
        print("you lost")

if __name__ == '__main__':
    main_menu()
