import sys  #for using exit

def displayboard(board):    #function for displaying the playing board
    print(board[0]+'  |  '+board[1]+'|  '+board[2])
    print('   '+'|'+'   '+'|'+'   ')
    print('   '+'|'+'   '+'|'+'   ')
    print('-----------')
    print(board[3]+'  |  '+board[4]+'|  '+board[5])
    print('   '+'|'+'   '+'|'+'   ')
    print('   '+'|'+'   '+'|'+'   ')
    print('-----------')
    print(board[6]+'  |  '+board[7]+'|  '+board[8])
    print('   '+'|'+'   '+'|'+'   ')
    print('   '+'|'+'   '+'|'+'   ')


def cont(win):  #function for asking players whether they want to play another game or not
    if win==True:   #if any player wins the game,ask if they want to continue,else,continue the loop
         print('do you want to continue?(y for yes/n for no)')
         resp=input()
         win=False  #new game,so initialise winner to none
         global board
         board=[' ']*9  #clear the board for a new game
         global posfill
         posfill=[]*9   #positions should be empty for a new game
         while (resp!='y' and resp!='n') and len(resp)!=1:
             print('enter a valid code')
             resp=input()
         return resp    #returning response of player
    else:
         pass


win=False   #for checking whether any player has won the game or not
posfill=[]*9   #for keeping track of positions in playing board which are already filled
board=[' ']*9   #this list will store the responses of both the players for filling the playing board
mark=False   #variable for checking the correct symbol 
print('enter the marker of the first player(X OR O)')
player1=input()


if player1=='X' or player1=='O':
    mark=True

    
while mark==False:   #loop will go on until user enters the correct symbol
    print('enter a valid marker for the first player(X OR O)')
    player1=input()
    if player1=='X' or player1=='O':
        mark=True


if player1=='X':    #for assigning symbol to player2
    player2='O'
else:
    player2='X'


print('are you ready to play the game(y for yes/n for no)')
resp=input()
while (resp!='y' and resp!='n') and len(resp)!=1:   #for checking whether player wants to play the game or not
    print('enter a valid code')
    resp=input()

displayboard(board)

while resp!='n':    #the loop will go on until the player continues the game
    
    print('enter the position in which player 1 wants to insert the marker(1-9)(1 starts from top left)')
    pos=int(input())
    
    while (pos>9 or pos<1) or (pos in posfill):   #for checking whether player 1 has inserted correct position and whether the position is already filled or not
        print('invalid position')
        print('enter the position in which player 1 wants to insert the marker(1-9)(1 starts from top left)')
        pos=int(input())
    posfill.append(pos)

    board[pos-1]=player1
    

    if ((board[0]==player1 and board[1]==player1 and board[2]==player1) or #first row
        (board[3]==player1 and board[4]==player1 and board[5]==player1) or #second row
        (board[6]==player1 and board[7]==player1 and board[8]==player1) or #third row
        (board[0]==player1 and board[3]==player1 and board[6]==player1) or #first column
        (board[1]==player1 and board[4]==player1 and board[7]==player1) or #second column
        (board[2]==player1 and board[5]==player1 and board[8]==player1) or #third column
        (board[0]==player1 and board[4]==player1 and board[8]==player1) or #first diagonal
        (board[2]==player1 and board[4]==player1 and board[6]==player1)): #second diagonal
        print('congratulations,player 1 wins')
        win=True
        resp=cont(win)
        continue
    else:
        pass

    if len(posfill)==9: #playing board is full,so it is a draw and we ask players if they want to play another game
        print('its a draw')
        resp=cont(True)
        continue
    else:
        pass
    
    displayboard(board)

    print('enter the position in which player 2 wants to insert the marker(1-9)(1 starts from top left)')
    pos=int(input())
    
    while (pos>9 or pos<1) or (pos in posfill):   #for checking whether player 2 has inserted correct position and whether the position is already filled or not
        print('invalid position')
        print('enter the position in which player 2 wants to insert the marker(1-9)(1 starts from top left)')
        pos=int(input())
    posfill.append(pos)

    board[pos-1]=player2
    
    
    if ((board[0]==player2 and board[1]==player2 and board[2]==player2) or #first row
        (board[3]==player2 and board[4]==player2 and board[5]==player2) or #second row
        (board[6]==player2 and board[7]==player2 and board[8]==player2) or #third row
        (board[0]==player2 and board[3]==player2 and board[6]==player2) or #first column
        (board[1]==player2 and board[4]==player2 and board[7]==player2) or #second column
        (board[2]==player2 and board[5]==player2 and board[8]==player2) or #third column
        (board[0]==player2 and board[4]==player2 and board[8]==player2) or #first diagonal
        (board[2]==player2 and board[4]==player2 and board[6]==player2)): #second diagonal
        print('congratulations,player 2 wins')
        win=True
        resp=cont(win)
        continue
    else:
        pass

    if len(posfill)==9: #playing board is full,so it is a draw and we ask players if they want to play another game
        print('its a draw')
        resp=cont(True)
        continue
    else:
        pass

    displayboard(board)
    



    

            



    
   
          


