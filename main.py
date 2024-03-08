#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Troppo alto")
        return turns - 1
    elif guess < answer:
        print("Troppo basso")
        return turns - 1
    else:
        print(f"Hai indovinato il numero era {answer}")


def set_difficulty():
    level = input("Scegli la difficoltà. Scegli 'facile' o 'difficile': ")
    if level == "facile":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Benvenuto a 'Indovina il numero'!")
    turns = set_difficulty()
    print("Sto pensando a un numero tra 1 e 100.")
    answer = random.randint(1, 100)

    
    guess = 0
    while guess != answer:
        print(f"Hai {turns} tentativi rimasti per indovinare il numero.")
        guess = int(input("Scegli un numero: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Hai esaurito i tentativi, hai perso")
            return
        elif guess != answer:
            print("Riprova")


game()
