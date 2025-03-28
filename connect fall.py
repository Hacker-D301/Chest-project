import random

def move(map, round, up1, up2):
     map_print(map)
     if round == 0:
          playermove1_width = int(input('player1 please set your position'))
          if playermove1_width == mark[playermove1_width] and up1[playermove1_width] != 0:
               up1[playermove1_width] = up1[playermove1_width] - 1
               map[up1[playermove1_width]][playermove1_width] = '1'
          else:     
               map[up1[playermove1_width]][playermove1_width] = '1'
          mark[playermove1_width] = playermove1_width
     if round == 1:
          playermove2_width = int(input('player2 please set your position'))
          if playermove2_width == mark[playermove2_width] and up2[playermove2_width] != 0:
               up2[playermove2_width] = up2[playermove2_width] - 1
               map[up2[playermove2_width]][playermove2_width] = '2'
          else:
               map[up2[playermove2_width]][playermove2_width] = '2'
          mark[playermove2_width] = playermove2_width
     map_print(map)
     return map

def count_check(map, win):
     player1_wincount = 0
     player2_wincount = 0
     for j in range(0, 5):
          player1_wincount = 0
          player2_wincount = 0
          for i in range(0, 5):
              if map[i][j] == '1':
                  player1_wincount = player1_wincount + 1
              if map[i][j] == '2':
                  player2_wincount = player2_wincount + 1
     if player1_wincount == 5:
         win = 1
     if player2_wincount == 5:
         win = 2
     player1_wincount = 0
     player2_wincount = 0
     for i in range(0, 5):
          player1_wincount = 0
          player2_wincount = 0
          for j in range(0, 5):
              if map[i][j] == '1':
                  player1_wincount = player1_wincount + 1
              if map[i][j] == '2':
                  player2_wincount = player2_wincount + 1
     if player1_wincount == 5:
         win = 1
     if player2_wincount == 5:
         win = 2
     player1_wincount = 0
     player2_wincount = 0
     i = 0
     j = 0
     while i < 5 and j < 5:
       if map[i][j] == '1':
              player1_wincount = player1_wincount + 1
       if map[i][j] == '2':
              player2_wincount = player2_wincount + 1
       i = i + 1
       j = j + 1
     if player1_wincount == 5:
         win = 1
     if player2_wincount == 5:
         win = 2
     i = 4
     j = 4
     while i>-1 and j>-1:
       if map[i][j] == '1':
              player1_wincount = player1_wincount + 1
       if map[i][j] == '2':
              player2_wincount = player2_wincount + 1
       i = i - 1
       j = j - 1
     if player1_wincount == 5:
         win = 1
     if player2_wincount == 5:
         win = 2
     player1_wincount = 0
     player2_wincount = 0
     return win

def round_check(round):
     if round == 0:
          round = 1
          return round
     if round == 1:
          round = 0
          return round

def win_count(win):
     if win == 1:
          print('player1 win!')
     if win == 2:
          print('player2 win!')

def map_print(map):
     for i in range(0, 5):
          print(map[i])  
     print("--------------------------------------")   

mark:list = [""]*5
up1:list = [4, 4, 4, 4, 4]
up2:list = [4, 4, 4, 4, 4] 
win = 0
map = [['0','0','0','0','0'],
       ['0','0','0','0','0'],
       ['0','0','0','0','0'],
       ['0','0','0','0','0'],
       ['0','0','0','0','0']]

round = random.randint(0, 1)

map = move(map, round, up1, up2)
win = count_check(map, win)
win_count(win)
round = round_check(round)
while win == False:
     map = move(map, round, up1, up2)
     win = count_check(map, win)
     win_count(win)
     round = round_check(round)