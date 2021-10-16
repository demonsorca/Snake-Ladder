import GameBoard as GB
import pygame as p

p.init()
p.display.set_caption("Snake-Ladder Game")


WIDTH = HEIGHT = 840
DIMENSION = 10
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
DICE = {}

mat = [
            ['100', '99', '98', '97', '96', '95', '94', '93', '92', '91'],
            ['81', '82', '83', '84', '85', '86', '87', '88', '89', '90'],
            ['80', '79', '78', '77', '76', '75', '74', '73', '72', '71'],
            ['61', '62', '63', '64', '65', '66', '67', '68', '69', '70'],
            ['60', '59', '58', '57', '56', '55', '54', '53', '52', '51'],
            ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50'],
            ['40', '39', '38', '37', '36', '35', '34', '33', '32', '31'],
            ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
            ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        ]
pos = {}
x = y = 0
for i in range(10):
    for j in range(10):
        pos[int(mat[i][j])] = [x + SQ_SIZE*j, y + SQ_SIZE*i]

screen = p.display.set_mode((WIDTH+240,HEIGHT))
boardImage = p.image.load('Images/Board.jpg')
boardImage = p.transform.scale(boardImage,(WIDTH,HEIGHT))
dice = p.image.load('Images/dice-6.svg')
dice = p.transform.scale(dice,(80,80))


def loadImages():
    for piece in range(1,7):
        DICE[piece] = (p.transform.scale(p.image.load("Images/dice-"+str(piece)+".svg"), (80,80)))
def main():
    #Dice
    dices = GB.Dice(1)

    # Players
    p1 = GB.Player("RED",1,"r")
    p2 = GB.Player("BLUE",2,"b")

    # List of Players
    players = []
    players.append(p1)
    players.append(p2)

    # Making Snake objects
    snake1 = GB.Jumper(45,5)
    snake2 = GB.Jumper(52,35)
    snake3 = GB.Jumper(67,28)
    snake4 = GB.Jumper(90,50)
    snake5 = GB.Jumper(99,24)
    snake6 = GB.Jumper(23,17)
    # Making Ladder objects
    ladder1 = GB.Jumper(8,29)
    ladder2 = GB.Jumper(22,61)
    ladder3 = GB.Jumper(65,97)
    ladder4 = GB.Jumper(72,93)

    # list of Snakes and Ladders
    snakeOrLadder = []
    snakeOrLadder.append(snake1)
    snakeOrLadder.append(snake2)
    snakeOrLadder.append(snake3)
    snakeOrLadder.append(snake4)
    snakeOrLadder.append(snake5)
    snakeOrLadder.append(snake6)

    snakeOrLadder.append(ladder1)
    snakeOrLadder.append(ladder2)
    snakeOrLadder.append(ladder3)
    snakeOrLadder.append(ladder4)

    # Calling Game Engine
    gb = GB.GameBoard(players,snakeOrLadder,dices,100)
    gb.startGame()

def drawGameState(player,diceVal,players):
    screen.fill((0, 0, 1))
    screen.blit(boardImage, (0,0))
    screen.blit(DICE[diceVal], (WIDTH+40, HEIGHT//2))
    font = p.font.SysFont('Helvitca',46,True,False)
    font2 = p.font.SysFont('Helvitca',25,False,False)

    text1 = font.render("Player "+player.PlayerName,0,p.Color('Blue'))
    text2 = font.render("Turn",0,p.Color('Blue'))
    text3 = font2.render("Tap anywhere to roll the dice.",0,p.Color('Yellow'))

    screen.blit(text1,(WIDTH+20, (HEIGHT//2)-70))
    screen.blit(text2,(WIDTH+20, (HEIGHT//2)-40))
    screen.blit(text3,(WIDTH+10, HEIGHT-40))

    drawPlayerPosition(players)
    drawDice(diceVal)

def drawPlayerPosition(players):
    for player in players:
        image = p.transform.scale(p.image.load(player.playerGoti), (SQ_SIZE, SQ_SIZE))
        screen.blit(image,(pos[player.currentPosition][0],pos[player.currentPosition][1]))

def drawDice(diceVal):
    screen.blit(DICE[diceVal], (WIDTH+40, HEIGHT//2))

def winner(player):
    font = p.font.SysFont('Helvitca', 46, True, False)
    text = font.render("Player " + player.PlayerName+" Wins", 0, p.Color('Blue'))
    screen.blit(text, (WIDTH//4, (HEIGHT//2)-20))



if __name__ == "__main__":
    main()