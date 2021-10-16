import random
import time
import Game as G
import pygame as p

class GameBoard():
    def __init__(self,players,snakeOrLadder,dices,boardSize):
        self.dices = dices
        self.boardSize = boardSize
        self.players = players
        self.snakeOrLadder = snakeOrLadder
        self.count = 0

    def startGame(self):
        running = True
        diceVal = 2
        while running:
            G.loadImages()
            turn = self.count % len(self.players)
            player = self.players[turn]
            G.drawGameState(player,diceVal,self.players)
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    diceVal = self.dices.rollDice()
                    G.drawGameState(player,diceVal,self.players)
                    p.display.flip()
                    nextCell = player.currentPosition + diceVal
                    if nextCell > self.boardSize:
                        pass
                    elif nextCell == self.boardSize:
                        print(player.PlayerName, "Win")
                        player.currentPosition = nextCell
                        G.drawGameState(player, diceVal, self.players)
                        G.winner(player)
                        p.display.flip()
                        time.sleep(10)
                        running = False
                    else:
                        flag = False
                        for cell in self.snakeOrLadder:
                            if cell.startPoint == nextCell:
                                flag = True
                                player.currentPosition = cell.endPoint
                                if cell.endPoint<cell.startPoint:
                                    print(player.PlayerName, "Bitten by Snake")
                                else:
                                    print(player.PlayerName, "Taken Ladder")
                        if not flag:
                            player.currentPosition = nextCell
                    print(player.PlayerName, "is at", player.currentPosition)
                    if diceVal!=6:
                        self.count += 1
            p.display.flip()


class Player():
    def __init__(self,PlayerName,id,color):
        self.PlayerName = PlayerName
        self.id = id
        self.playerGoti = "Images/" + color + "P.png"
        self.currentPosition = 1

class Dice():
    def __init__(self,numberOfDice):
        self.numberOfDice = numberOfDice

    def rollDice(self):
        return random.randint(self.numberOfDice*1,self.numberOfDice*6)

class Jumper():
    def __init__(self,startPoint,endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint



