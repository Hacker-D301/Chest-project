import random

map=(["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "", "", ""])

def map_print(map):
    i = 0
    while i<5: #map print
        list1 = list(map)
        print(list1[i])
        i = i + 1

def player_move(map):
    length = 0
    width = 0
    player_round: bool = True
    while player_round:
        length = int(input("please select the length -1 -2 -3 -4 -5"))
        width = int(input("please select the length -1 -2 -3 -4 -5"))
        check: bool = True
        if map[length-1][width-1] != "C":
            map[length-1][width-1] = "P"
            player_round = False
    map_print(map)

def com_move(map):
    length = 0
    width = 0
    player_round: bool = True
    while player_round:
        length = random.randint(0, 4)
        width = random.randint(0, 4)
        check: bool = True
        if map[length-1][width-1] != "P":
            map[length-1][width-1] = "C"
            player_round = False
    map_print(map)

def win_chack_COM(map, turn):
    count = 0
    length = 0
    width = 0
    x = 0
    y = 0
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+x][width] == "C" and map[length][width+y] == "C":
                count = count + 1
                turn = False
                return(count)
           
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+y][width] == "C" and map[length][width+x] == "C":
                count = count + 1
                turn = False
                return(count)
            
    while x and y < 5:#left to right slop check
        if map[length+y][width] == "C" and map[length][width+x] == "C":
            count = count + 1
            turn = False
            return(count)
        else:
            x = x + 1
            y = y + 1
        
    #rlcheck:bool = True
    x = 4
    y = 0
    while x and y < 5:#right to left slop check
        if map[length+y][width] == "C" and map[length][width+x] == "C":
            count = count + 1
            #rlcheck = False
            turn = False
            return(count)
        else:
            x = x - 1
            y = y + 1
        
    if win:
        print("com win!")

def check_count(count):
    win:bool = False
    if count == 5:
        win = True
        return(win)
    else:
        count = 0

def win_chack_player(map, turn):
    count = 0
    length = 0
    width = 0
    x = 0
    y = 0
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+x][width] == "P" and map[length][width+y] == "P":
                count = count + 1
                turn = False
                return(count)
           
    for x in range(0, 4):
        for y in range(0, 4):
            if map[length+y][width] == "P" and map[length][width+x] == "P":
                count = count + 1
                turn = False
                return(count)
             
    while x and y < 5:#left to right slop check
        if map[length+y][width] == "P" and map[length][width+x] == "P":
            count = count + 1
            turn = False
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
            turn = False
            return(count)
        else:
            x = x - 1
            y = y + 1
    if win:
        print("player win!")
    
#--------------------------------------------------------------------------------------------------

c = random.randint(0, 1)
turn:bool = True
if c == 1:
        print("player turn")
        player_move(map)
else:
        print("COM turn")
        com_move(map)
while turn:
   if c == 1:
       c = 0
   else:
       c = 1
   if c == 1:
       print("player turn")
       player_move(map)
   else:
       print("COM turn")
       com_move(map)
   
   count = win_chack_player(map, turn)
   win = check_count(count)
   count = win_chack_COM(map, turn)
   win = check_count(count)