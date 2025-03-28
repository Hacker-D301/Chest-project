import random

def move(round, map):
    if round == 1:
        map_print(map)
        print("set your step!")
        playerMove_lengh = int(input("length:"))
        playerMove_width = int(input("width:"))
        comMove_lengh = comMove_width = 0
    if round == 0:
        comMove_lengh = random.randint(0, 4)
        comMove_width = random.randint(0, 4)
        playerMove_lengh = playerMove_width = 0
    return playerMove_lengh, playerMove_width, comMove_lengh, comMove_width

def map_show_and_change(round, map, playerMove_lengh, playerMove_width, comMove_lengh, comMove_width):
    if round == 1 and map[playerMove_lengh][playerMove_width] != "C":
        map[playerMove_lengh][playerMove_width] = "P"
    if round == 0 and map[playerMove_lengh][playerMove_width] != "P":
        map[comMove_lengh][comMove_width] = "C"
    newmap:list = map
    return newmap

def attack_count(map):
    new_player_count = 0
    new_com_count = 0
    palyer_mark_i:list = [0]*5
    player_mark_j:list = [0]*5
    com_mark_i:list = [0]*5
    com_mark_j:list = [0]*5
    i = 0
    j = 0
    play_c:str = 0
    com_c:str = 0
    if new_player_count < 5 or new_com_count < 5:
        for i in range(0, 5):#length
            for j in range(0, 5):
                if map[i][j] == "P":
                    new_player_count = new_player_count + 1
                    palyer_mark_i[play_c+j] = i
                    player_mark_j[play_c+j] = j
                if map[i][j] == "C":
                    new_com_count = new_com_count + 1
                    com_mark_i[com_c+j] = i
                    com_mark_j[com_c+j] = j
            if  new_player_count == 5 or new_com_count == 5:
                if new_player_count < 5:
                    new_player_count, palyer_mark_i, player_mark_j = 0, [0]*5, [0]*5
                if new_com_count < 5:
                    new_com_count, com_mark_i, com_mark_j = 0, [0]*5, [0]*5
                return new_player_count, new_com_count, palyer_mark_i, player_mark_j, com_mark_i, com_mark_j
            else:
                new_player_count = 0
                new_com_count = 0
        i = 0
        j = 0
        palyer_mark_i:list = [0]*5
        player_mark_j:list = [0]*5
        com_mark_i:list = [0]*5
        com_mark_j:list = [0]*5
        for j in range(0, 5):#width
            for i in range(0, 5):
                if map[i][j] == "P":
                    new_player_count = new_player_count + 1
                    palyer_mark_i[play_c+i] = i
                    player_mark_j[play_c+i] = j
                if map[i][j] == "C":
                    new_com_count = new_com_count + 1
                    com_mark_i[com_c+i] = i
                    com_mark_j[com_c+i] = j
            if  new_player_count == 5 or new_com_count == 5:
                if new_player_count < 5:
                    new_player_count, palyer_mark_i, player_mark_j = 0, [0]*5, [0]*5
                if new_com_count < 5:
                    new_com_count, com_mark_i, com_mark_j = 0, [0]*5, [0]*5
                return new_player_count, new_com_count, palyer_mark_i, player_mark_j, com_mark_i, com_mark_j
        else:
            new_player_count = 0
            new_com_count = 0
        i = 0
        j = 0
        palyer_mark_i:list = [0]*5
        player_mark_j:list = [0]*5
        com_mark_i:list = [0]*5
        com_mark_j:list = [0]*5
        while i<5 and j<5:
            if map[i][j] == "P":
                new_player_count = new_player_count + 1
                palyer_mark_i[play_c+i] = i
                player_mark_j[play_c+j] = j
            if map[i][j] == "C":
                new_com_count = new_com_count + 1
                com_mark_i[com_c+i] = i
                com_mark_j[com_c+j] = j
            i = i + 1
            j = j + 1
            if  new_player_count == 5 or new_com_count == 5:
                if new_player_count < 5:
                    new_player_count, palyer_mark_i, player_mark_j = 0, [0]*5, [0]*5
                if new_com_count < 5:
                    new_com_count, com_mark_i, com_mark_j = 0, [0]*5, [0]*5
                return new_player_count, new_com_count, palyer_mark_i, player_mark_j, com_mark_i, com_mark_j
        i = 4
        j = 4
        palyer_mark_i:list = [0]*5
        player_mark_j:list = [0]*5
        com_mark_i:list = [0]*5
        com_mark_j:list = [0]*5
        while i>0 and j>0:
            if map[i][j] == "P":
                new_player_count = new_player_count + 1
                palyer_mark_i[play_c+i] = i
                player_mark_j[play_c+j] = j
            if map[i][j] == "C":
                new_com_count = new_com_count + 1
                com_mark_i[com_c+i] = i
                com_mark_j[com_c+j] = j
            i = i - 1
            j = j - 1
        if  new_player_count == 5 or new_com_count == 5:
                if new_player_count < 5:
                    new_player_count, palyer_mark_i, player_mark_j = 0, [0]*5, [0]*5
                if new_com_count < 5:
                    new_com_count, com_mark_i, com_mark_j = 0, [0]*5, [0]*5
                    return new_player_count, palyer_mark_i, player_mark_j, new_com_count, com_mark_i, com_mark_j
    new_player_count, palyer_mark_i, player_mark_j, new_com_count, com_mark_i, com_mark_j = 0, [0]*5, [0]*5, 0, [0]*5, [0]*5
    return new_player_count, palyer_mark_i, player_mark_j, new_com_count, com_mark_i, com_mark_j

def attack_map_change(new_player_count, new_com_count, player_mark_i, player_mark_j, com_mark_i, com_mark_j, player_hp, com_hp, map):
    c = 0
    player_hit = 0
    com_hit = 0
    if new_player_count == 5:
        player_hit = 5
        while c<5:
            i = player_mark_i[c]
            j = player_mark_j[c]
            map[i][j] = "A"
            c = c + 1
        comMove_lengh = random.randint(0, 4)
        comMove_width = random.randint(0, 4)
        if map[comMove_lengh][comMove_width] == "A":
            player_hit = player_hit - 1
        com_hp = com_hp - player_hit
    if new_com_count == 5:
        com_hit = 5
        while c<5:
            i = com_mark_i[c]
            j = com_mark_j[c]
            map[i][j] = "A"
            c = c + 1
        playerMove_lengh = input("length:")
        playerMove_width = input("width:")
        if map[playerMove_lengh][playerMove_width] == "A":
            player_hit = player_hit - 1
        player_hp = player_hp - com_hit
    return player_hp, com_hp

def win_check(player_hp, com_hp, player_win, com_win):
    if player_hp <= 0:
        print("COM win!")
        com_win = True
    if com_hp <=0:
        print("PLAYER WIN!")
        player_win = True
    return player_win, com_win

def round_check(round):
    if round == 0:
        round = 1
        return round
    if round == 1:
        round = 0
        return round

def map_print(map):
    for i in range(0, 5):
        map_p = map[i]
        print(map_p)

#----------------------------
map:list = [["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ]

player_hp = 5
com_hp = 5
round = random.randint(0, 1)
player_win = False
com_win = False
while player_win == False or com_win == False:
    playerMove_lengh, playerMove_width, comMove_lengh, comMove_width = move(round, map)
    map = map_show_and_change(round, map, playerMove_lengh, playerMove_width, comMove_lengh, comMove_width)
    new_player_count, new_com_count, player_mark_i, player_mark_j, com_mark_i, com_mark_j = attack_count(map)
    player_hp, com_hp = attack_map_change(new_player_count, new_com_count, player_mark_i, player_mark_j, com_mark_i, com_mark_j, player_hp, com_hp, map)
    player_win, com_win = win_check(player_hp, com_hp, player_win, com_win)
    round = round_check(round)