#Trying to program a console tic-tac-toe game

#Square brackets means list (which is mutable)
#Parentheses represents tuple (which is immutable)
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

print("   0  1  2")
count = 0
for row in game:
    #To print multiple things, simply put as separate parameters
    print(count, row)
    count+=1


