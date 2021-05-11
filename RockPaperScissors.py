"""ROCK PAPER SCISSORS"""

import random
import re
import os


class Player:
    def __init__(self):
        self.score = 0

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def incrementscore(self):
        self.score = self.score + 1

class Human(Player):
    pass
class Bot(Player):
    pass


def checkResult(userChoice, opponentChoice, player, bot):
    if opponentChoice == str.upper(userChoice):
        print("Tie!")
        return
    elif opponentChoice == 'R' and userChoice.upper() == 'S':
        print("Rock beats scissors, I win!")
        updateScores(False, player, bot)
        return
    elif opponentChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper, I win!")
        updateScores(False, player, bot)
        return
    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beats Rock, I win!")
        updateScores(False, player, bot)
        return
    else:
        print("You win!")
        updateScores(True, player, bot)


def promptRestart():
    userInput = input("Do you want to restart? [Y]es, [N]o: ")
    userInput = verifyUserInput("[YyNn]", userInput)
    if userInput.upper() == 'Y':
        print("Restarting game...")
        return True
    elif userInput.upper() == 'N':
        print("Thank you for playing!")
        return False

def showFinalScore(player, bot):
    print("\n--- FINAL RESULT ---")
    print("Player score: " + str(player.getScore()) + "; Bot score: " + str(bot.getScore()))


def gameLogic(player, bot):
    print("\nRock, Paper, Scissors - Shoot!")
    userChoice = input("\nChoose your weapon [R]ock, [P]aper, [S]cissors: ")
    userChoice = verifyUserInput("[RrPpSs]", userChoice)
    print("You chose: " + userChoice.upper())
    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)
    print("I chose: " + opponentChoice)
    checkResult(userChoice, opponentChoice, player, bot)


def startGame():
    player = Human()
    bot = Bot()
    restart = True
    while (restart):
        gameLogic(player, bot)
        restart = promptRestart()
    showFinalScore(player, bot)


def verifyUserInput(expectedInput, userInput):
    correctInput = False
    while (correctInput == False):
        if not re.match(expectedInput, userInput):
            print("Please choose a valid option.")
            userInput = input()
            verifyUserInput(expectedInput, userInput)
        else:
            correctInput = True
    return userInput


def updateScores(playerVictory, player, bot):
    if (playerVictory):
        player.incrementscore()
    else:
        bot.incrementscore()
    print("\nPlayer score: " + str(player.getScore()) + "; Bot score: " + str(bot.getScore()))


startGame()
