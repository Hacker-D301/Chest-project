import random

map=(["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "C", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""])

def win_chack_COM(map):#bug it cannot really found the C
    count = 0
    length = 0
    width = 0
    x = 0
    y = 0
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+x][width] == "C" and map[length][width+y] == "C":
                count = count + 1
                return(count)
            print("found")
           
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+y][width] == "C" and map[length][width+x] == "C":
                count = count + 1
                return(count)
            print("found")
            
    while x and y < 5:#left to right slop check
        if map[length+y][width] == "C" and map[length][width+x] == "C":
            count = count + 1
            return(count)
        else:
            x = x + 1
            y = y + 1
        print("found")
    #rlcheck:bool = True
    x = 4
    y = 0
    while x and y < 5:#right to left slop check
        if map[length+y][width] == "C" and map[length][width+x] == "C":
            count = count + 1
            #rlcheck = False
            return(count)
        else:
            x = x - 1
            y = y + 1
        print("found")
    #if win:
        #print("com win!")

def check_count(count):
    win:bool = False
    if count == 5:
        win = True
        return(win)
    else:
        count = 0

def win_chack_player(map):#bug:In check time,the loop will stop in loop 1
    count = 0
    length = 0
    width = 0
    x = 0
    y = 0
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+x][width] == "P" and map[length][width+y] == "P":
                count = count + 1
                return(count)
           
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+y][width] == "P" and map[length][width+x] == "P":
                count = count + 1
                return(count)
             
    while x and y < 5:#left to right slop check
        if map[length+y][width] == "P" and map[length][width+x] == "P":
            count = count + 1
            return(count)
        else:
            x = x + 1
            y = y + 1

    #rlcheck:bool = True
    x = 4
    y = 0
    while x and y < 5:#right to left slop check
        if map[length+y][width] == "P" and map[length][width+x] == "P":
            count = count + 1
            #rlcheck = False
            return(count)
        else:
            x = x - 1
            y = y + 1
    #if win:
        #print("player win!")

#count = win_chack_player(map)
#win = check_count(count)
count = win_chack_COM(map)
#win = check_count(count)