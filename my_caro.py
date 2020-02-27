import turtle
import random
import math

global move_history
turn = 'w'
moveCount = 0

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

# def is_empty(board):
#     return board == [[' ']*len(board)]*len(board)

def is_in(board, y, x):
    return 0 <= y < len(board) and 0 <= x < len(board)

def belongToLine(y, x):
    d = 0
    for i in range(4):
        if y + i < 15:
            if(board[y + i][x] !=  board[y][x]):
                break
            d += 1
    for i in range(4):
        if y - i > -1:
            if(board[y - i][x] !=  board[y][x]):
                break
            d += 1
    if d >= 5:
        return True
    
    d = 0
    for i in range(4):
        if x + i < 15:
            if board[y][x + i] !=  board[y][x]:
                break
            d += 1
    for i in range(4):
        if x - i > -1:
            if board[y][x - i] !=  board[y][x]:
                break
            d += 1
    if d >= 5:
        return True
    
    d = 0
    for i in range(4):
        if y + i < 15 and x + i < 15:
            if(board[y + i][x + i] !=  board[y][x]):
                break
            d += 1
    for i in range(4):
        if y - i > -1 and x - i > -1:
            if board[y - i][x - i] !=  board[y][x]:
                break
            d += 1
    if d >= 5:
        return True

    d = 0
    for i in range(4):
        if y + i < 15 and x - i > -1:
            if(board[y + i][x - i] != board[y][x]):
                break
            d += 1
    for i in range(4):
        if y - i > -1 and x + i < 15:
            if board[y - i][x + i] !=  board[y][x]:
                break
            d += 1
    if d >= 5:
        return True

    return False

def is_win(board, recentY, recentX):
    if moveCount != size**2:
        if belongToLine(recentY, recentX):
            if board[recentY][recentX] == 'b':
                return 'Black won'
            else:
                return 'White won'
    else:    
        return 'Draw'
        
    return 'Continue playing'

def exitButton():
    button = turtle.Turtle()
    button.penup()
    button.goto(7, 7)
    button.pendown()
    button.begin_fill
    button.color('blue')  
    button.circle(2)
    button.end_fill()
    button.penup()
    button.goto(7, 10)
    button.pendown()
    button.color('orange')
    button.write('CLICK\n TO EXIT', True, align = 'center', font=("Arial", 15, "normal"))


def clickOnButton(x, y):
    if math.sqrt((x - 7)**2 + (y - 8)**2) <= 2:
        turtle.Screen().bye()   # exit when clicked in right place
    else:
        return


def click(x, y):
    global board, colors, win, move_history, turn, moveCount
    x, y = getIndexPos(x, y)
    if x == -1 and y == -1 and len(move_history) != 0:
        x, y = move_history[-1]
        del(move_history[-1])
        board[y][x] = ' '
        x, y = move_history[-1]
        return
    
    if not is_in(board, y, x):
        return 
    
    if board[y][x] == ' ':
        if turn == 'b':
            drawStone(x, y, colors['b'])
            board[y][x] = 'b'
            moveCount += 1
            turn = 'w'
        else:
            drawStone(x, y, colors['w'])
            board[y][x] = 'w'
            moveCount += 1
            turn = 'b'

        game_res = is_win(board, y, x)
        if game_res in ["White won", "Black won", "Draw"]:
            result =  turtle.Turtle()
            result.penup()
            result.sety(0)
            result.setx(10)
            result.color('navy')
            result.write(game_res, True, align = 'center', font=("Arial", 20, "italic"))
            print (game_res)
            win = True
            exitButton()
            turtle.Screen().onclick(clickOnButton)
            #turtle.Screen().exitonclick()   # exit graphic windowon click
            return


def initialize(size):
    global win, board, screen, colors

    moveHistory = []
    win = False
    board = make_empty_board(size)  # bang luu tru gia tri

    screen = turtle.Screen()
    screen.title('Tix Tac Toe')
    screen.onclick(click)
    screen.setup(screen.screensize()[1]*2, screen.screensize()[1]*2)
    screen.setworldcoordinates(-1, size, size, -1)
    screen.bgcolor('red')
    screen.tracer(500)
    screen.update()

    colors = {'b':turtle.Turtle(), 'w':turtle.Turtle()}
    colors['b'].color('black')
    colors['w'].color('white')

    for keys in colors:
        colors[keys].ht()   # hide turtle
        colors[keys].penup()
        colors[keys].speed(0)

    border = turtle.Turtle()
    border.speed(9)
    border.penup()

    side = round((size - 1) / 2)

    i = -1
    for start in range(size):
        border.goto(start, side + side*i)
        border.pendown()
        i *= -1
        border.goto(start, side + side*i)
        border.penup()

    i = -1
    for start in range(size):
        border.goto(side + side*i, start)
        border.pendown()
        i *= -1
        border.goto(side + side*i, start)
        border.penup()

    border.ht()

    screen.listen()   
    screen.mainloop()


def getIndexPos(x, y):
    X = int(round(x))
    Y = int(round(y))
    return X, Y


def drawStone(x, y, colturtle):
    colturtle.goto(x, y - 0.3)
    colturtle.pendown()
    colturtle.begin_fill()
    colturtle.circle(0.3)
    colturtle.end_fill()
    colturtle.penup()

if __name__ == "__main__":
    global size
    size = int(input('Choose size: '))
    initialize(size)