import time
import random
#Trying to program a console tic-tac-toe game

#Square brackets means list (which is mutable)
#Parentheses represents tuple (which is immutable)
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]


def print_board():
    print("   a  b  c")
    for count, row in enumerate(game):
        #To print multiple things, simply put as separate parameters
        print(count, row)

def game_over():
    #Horizontal check
    for row in game:
        if 0 in row:
            continue
        if(row[0]==row[1] and row[1]==row[2] and not_zeroes(row[0],row[1],row[2])):
            #print("horizontal")
            return True
    #Vertical check, may not be the simplest way but it works
    row0 = game[0]
    row1 = game[1]
    row2 = game[2]
    i = 0
    for i in range(len(game[0])):
        if(row0[i]==row1[i] and row1[i]==row2[i] and not_zeroes(row0[i],row1[i],row2[i])):
            #print("vertical")
            return True

    #Diagonal check, there are only 2 cases so easy
    if(game[0][0]==game[1][1] and game[1][1]==game[2][2] and not_zeroes(game[0][0], game[1][1], game[2][2])):
        #print("diagonal")
        return True
    if(game[0][2]==game[1][1] and game[1][1]==game[2][0] and not_zeroes(game[0][2], game[1][1], game[2][0])):
        #print("diagonal")
        return True
    return False

def not_zeroes(val1, val2, val3):
    if(val1!=0 and val2!=0 and val3!=0):
        return True

def is_valid(val):
    if(val[0].isalpha()==False):
        return False
    if(val[1].isnumeric()==False):
        return False
    temp = 0
    if(val[0]=='a'):
        temp = 0
    if(val[0]=='b'):
        temp = 1
    if(val[0]=='c'):
        temp = 2
    if(int(val[1])>=len(game[0])):
        return False
    return game[int(val[1])][temp]==0

def change_coord(coord, value):
    temp = 0
    if(coord[0]=='a' or coord[0]=='0'):
        temp = 0
    if(coord[0]=='b' or coord[0]=='1'):
        temp = 1
    if(coord[0]=='c' or coord[0]=='2'):
        temp = 2
    game[int(coord[1])][temp] = value

def opponent_move():
    open_spots = ()
    for r_count, r in enumerate(game):
        for c_count, c in enumerate(r):
            if(game[r_count][c_count]==0):
                open_spots += (r_count,c_count)
    #print("Possible spots: ", open_spots)
    index = random.randrange(0, len(open_spots), 2)
    change_coord(str(open_spots[index])+str(open_spots[index+1]), 2)
    
print_board()
while game_over()==False:
    val = ""
    while True:
        val = input('Enter the coordinates: ')
        if(is_valid(val)):
            break
        else:
            print("Not valid!")
    change_coord(val, 1)
    print_board()
    if(game_over()):
        break
    time.sleep(1)
    opponent_move()
    print("The computer just moved!")
    print_board()
print("Game is finished!")


    
    


