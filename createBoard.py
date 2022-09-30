from createList import createListContent

top = '══'
top_right_corn = '╗'
low_right_corn = '╝'
side = '║'
top_left_corn = '╔'
low_left_corn = '╚'
space = ' '

data = createListContent()

def createGameBoard(board):
    for y in range(0, len(board)):
        ltop = ''
        lmiddle = ''
        lbottom = ''
        for x in range(0, len(board[y])):
            ltop += top_left_corn + top*2
            lmiddle += side + f'{x},{y}' + space
            lbottom += side + top*2
        else:
            ltop += top_right_corn
            lmiddle += side
            lbottom += low_right_corn
        print(ltop + '\n' + lmiddle + '\n' + lbottom)

createGameBoard(data)
