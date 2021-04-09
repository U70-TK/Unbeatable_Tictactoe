import os
import sys
import pygame
import time
import pyautogui as pg

def concat(lst):
    nlist = []
    for i in range(len(lst)):
        nlist += lst[i]
    return nlist

def chop(num,ls):
    """This function aims to take in a argument, 
    then chop it into different small lists that have a length of the given number."""
    def take(val,lst):
        empty = []
        for b in range(val):
            empty += [lst[b]]
        return empty
    newl = []
    for _ in range(int(len(ls)/num)):
        newl += [take(num,ls)]
        del ls[0:num]
    return newl

def next(player):
    if player == 'X':
        return ('O')
    elif player == 'O':
        return ('X')
    elif player == '':
        return ('')

def full(grid):
    concat_grid = concat(grid)
    result = True
    for i in range(len(concat_grid)):
        if concat_grid[i] == '':
            result = False
            break
        elif concat_grid[i] == 'X' or concat_grid[i] == 'O':
            result = True
    return result

def turn(grid):
    """player O takes first"""
    num_X = 0
    num_O = 0
    concat_grid = concat(grid)
    for i in range(len(concat_grid)):
        if concat_grid[i] == 'X':
            num_X += 1
        elif concat_grid[i] == 'O':
            num_O += 1
    if num_O <= num_X:
        return ('O')
    else:
        return ('X')
    
def cols(grid):
    """This function aims to show every column of a grid"""
    new_lst = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            new_lst += [grid [j] [i]]
    return chop(3,new_lst)

def diag1(grid):
    new_grid = []
    for i in range(len(grid)):
        new_grid += grid[i] [i]
    if len(new_grid) == 0:
        return ['','','']
    elif len(new_grid) == 1:
        return (new_grid + ['',''])
    elif len(new_grid) == 2:
        return (new_grid + [''])
    else:
        return new_grid

def reverse(un_list):
    """This function aims to reverse a list"""
    empty_list = []
    if un_list == []:
        return []
    else:
        for i in range(len(un_list)-1,0,-1):
            empty_list += [un_list[i]]
        return empty_list + [un_list[0]]

def diag2(grid):
    rev_grid = []
    for i in range(len(grid)):
        rev_grid += reverse(grid[i])
    rev_grid = chop(3,rev_grid)
    return diag1(rev_grid)

def diag(grid):
    return [diag1(grid)]+ [diag2(grid)] 
    
def is_all_equal(player,lst):
    boolean = True
    for i in range(len(lst)):
        if lst[i] != player:
            boolean = False
            break
        else:
            boolean = True
    return boolean

def all_lines(grid):
    return (grid + cols(grid) + diag(grid))

def wins(player,grid):
    bool_list = list(map(lambda x: is_all_equal(player,x),all_lines(grid)))
    return (any (bool_list))

def won(grid):
    return (wins('X',grid) or wins('O',grid))

def human_human(grid,player):
    pygame.init()      # 硬件准备
    color_white=(255,255,255) # 设置底色
    screen =pygame.display.set_mode([700,700]) #设置窗口大小
    back_image= pygame.image.load("background2.jpg") #导入背景
    pygame.display.set_caption("井字棋") # 设置标题
    X_image = pygame.image.load("X.png") # 导入x图像
    O_image = pygame.image.load('O.png') # 导入o图像
    Draw_image = pygame.image.load('draw.png') # 导入平局图像
    Restart_image = pygame.image.load('Restart1.png') # 导入重新开始游戏的提示图像
    screen.blit(back_image,(0,0)) #显示背景
    pos = None # 位置初始值设置为none
    win_draw_state = False      # True 代表已经有过win或者draw的状态，False代表尚还没有赢或者平局
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #退出事件
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标点击事件
                x,y = pg.position()    # 获得鼠标所在坐标的数值
                if 370 <= x < 599 and 206 <= y < 373:
                    if player == 'O' and win_draw_state == False: # 如果状态为False
                        pos = 0 # 则不进入这个循环，保持输出一个restart图片的状态
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(25,87))
                            player = next(player)
                            pos = None
                            if wins('O',grid):    # 判断输赢或者平局
                                screen.blit(O_image,(300,550))
                                win_draw_state = True # 如果有输赢或者平局就给她定义一个状态
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 0
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(25,87))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 599 <= x < 838 and 206 <= y < 373:
                    if player == 'O' and win_draw_state == False:
                        pos = 1
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(240,87))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 1
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(240,87))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 838 <= x < 1069 and 206 <= y < 373:
                    if player == 'O' and win_draw_state == False:
                        pos = 2
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(475,87))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 2
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(475,87))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 370 <= x < 599 and 373 <= y < 536:
                    if player == 'O' and win_draw_state == False:
                        pos = 3
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(25,250))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 3
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(25,250))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 599 <= x < 838 and 373 <= y < 536:
                    if player == 'O' and win_draw_state == False:
                        pos = 4
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(240,250))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 4
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(240,250))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 838 <= x < 1069 and 373 <= y < 536:
                    if player == 'O'and win_draw_state == False:
                        pos = 5
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(475,250))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 5
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(475,250))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 370 <= x < 599 and 536 <= y < 699:
                    if player == 'O' and win_draw_state == False:
                        pos = 6
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(25,420))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 6
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(25,420))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 599 <= x < 838 and 536 <= y < 699:
                    if player == 'O' and win_draw_state == False:
                        pos = 7
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(240,420))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X' and win_draw_state == False:
                        pos = 7
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(240,420))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                elif 838 <= x < 1069 and 536 <= y < 699:
                    if player == 'O'and win_draw_state == False:
                        pos = 8
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(O_image,(475,420))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
                    elif player == 'X'and win_draw_state == False:
                        pos = 8
                        if move(grid,pos,player) == []:
                            pos = None
                            continue
                        else:
                            grid = (move(grid,pos,player))
                            screen.blit(X_image,(475,420))
                            player = next(player)
                            pos = None
                            if wins('O',grid):
                                screen.blit(O_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif wins('X',grid):
                                screen.blit(X_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            elif full(grid):
                                screen.blit(Draw_image,(300,550))
                                win_draw_state = True
                                screen.blit(Restart_image,(0,350))
                            else:
                                continue
            else:
                pygame.display.update()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    human_human([['','',''],['','',''],['','','']],'O')
                elif keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit() 
                elif keys[pygame.K_l]:
                    human_or_comp()
                else:
                    continue

def valid(grid,pos):
    """This function checks whether it is valid to put a value in a certain place."""
    concat_grid = concat(grid)
    return (pos >= 0 and pos < 9 and (concat_grid [pos] == ''))

def move(grid,pos,player):
    concat_grid = concat(grid)
    if valid(grid,pos):
        concat_grid[pos] = player
        return chop(3,concat_grid)
    else:
        return []

def moves(grid,player):
    if won(grid):
        return []
    elif full(grid):
        return []
    else:
        return chop(3,concat([move(grid, i, player) for i in range(9)]))

def gametree(grid,player):
    possible_moves = moves(grid,player)
    leave = list(map(lambda x:gametree(x,next(player)),possible_moves))
    return [grid] + [leave]

def prune(level,lst):
    def show_node(lst):
        return lst[0]
    if level == 0:
        return [show_node(lst),[]]
    else:
        ts = lst[1]
        return [show_node(lst)] + [list(map(lambda x:prune(level-1,x),ts))]

def show_p(t):
    """[(a,p),[lst]]"""
    return (t[0] [1])

def maxplayer(lt):
    if ('X' in lt):
        return ('X')
    elif (not('X' in lt)) and ('' in lt):
        return ('')
    elif (not('X' in lt)) and (not('' in lt)):
        return ('O')

def minplayer(lt):
    if ('O' in lt):
        return ('O')
    elif (not('O' in lt)) and ('' in lt):
        return ('')
    elif ('O' not in lt) and ('' not in lt) and ('X' in lt):
        return ('X')

def minimax(lst):
    """minimax function labels the given list of grid with the potential winner."""
    if lst[1] == []:
        if wins('O',lst[0]):
            return [(lst[0],'O'),[]]
        elif wins('X',lst[0]):
            return [(lst[0],'X'),[]]
        else:
            return [(lst[0],''),[]]
    else:
        ts = lst[1]
        ts_ = list(map(minimax,ts))
        ps = list(map(lambda x: show_p(x),ts_))
        if turn(lst[0]) == 'O':
            return [(lst[0],minplayer(ps)), ts_]
        elif turn(lst[0]) == 'X':
            return [(lst[0],maxplayer(ps)), ts_]

def show_g(t):
    """[(g,p),[lst]]"""
    return (t[0] [0])

def lst2str(lst):
    new = ''
    for i in range(len(lst)):
        new += lst[i]
    return new

def one_O(grid):
    if lst2str(concat(grid)) == 'O':
        return True
    else:
        return False
"""
def scores(grid,player):
    def score1(grid):
"""
def find_O_pos(grid):
    if one_O:
        l = concat(grid)
        result = None
        for i in range(len(l)):
            if l[i] == 'O':
                result = i + 1
                break
            else:
                continue
        return result
    else:
        return ('ERROR')

def bestmove(grid,player):
    """This function aims to find
    the best move for the given grid and player."""
    if one_O(grid):
        if find_O_pos(grid) == 1:
            a = list(open('O1.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 2:
            a = list(open('O2.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 3:
            a = list(open('O3.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 4:
            a = list(open('O4.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 5:
            a = list(open('O5.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 6:
            a = list(open('O6.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 7:
            a = list(open('O7.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 8:
            a = list(open('O8.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
        elif find_O_pos(grid) == 9:
            a = list(open('O9.txt', 'r', encoding= 'utf-8'))
            tree = eval(a[0])
    else:
        tree = prune(9,gametree(grid,player))
    best = show_p(minimax(tree))
    ts = (minimax(tree)) [1]
    g_lst = []
    for t in ts:
        if show_p(t) == best:
            g_lst += show_g(t)
        else:
            continue
    g_lst = chop(3,g_lst)
    if len(g_lst) == 1:
        return g_lst[0]
    else:
        return heuristic(g_lst)

def scores_(grid):
    def score1(grid):
        all_line = all_lines(grid)
        s = 0
        for i in range(len(all_line)):
            if (all_line[i] == ['X','X','']) or (all_line[i] == ['','X','X']) \
                or (all_line[i] == ['X','','X']):
                s += 50
        return s

    def score2(grid):
        all_line = all_lines(grid)
        s = 0
        for i in range(len(all_line)):
            if all_line[i] == ['X','X','X']:
                s += 1000
        return s
    
    def score3(grid):
        all_line = all_lines(grid)
        s = 0
        for i in range(len(all_line)):
            if all_line[i] == ['','X','']:
                s += 5
        return s
    
    def score4(grid):
        all_line = all_lines(grid)
        s = 0
        for i in range(len(all_line)):
            if (all_line[i] == ['X','','']) or (all_line[i] == ['','X','']) or (all_line[i] == ['','','X']):
                s += 1
        return s
    return (score1(grid)+score2(grid)+score3(grid)+score4(grid))

def scores(lst):
    return list(map(lambda x:scores_(x),lst))

def find_max(lst):
    max_num = lst[0]
    count = 0
    for i in range(len(lst)):
        if lst[i] > max_num:
            max_num = lst[i] 
            count = i
        else:
            continue
    return count

def heuristic(lst):
    score = scores(lst)
    max_pos = find_max(score)
    return lst[max_pos]

def show_diff_pos(grid):
    if one_O(grid):
        if find_O_pos(grid) == 5:
            return 1
        else:
            return 5
    else:
        grid1 = concat(grid)
        grid2 = concat(bestmove(grid,'X'))
        pos = None
        for i in range(len(grid1)):
            if grid1[i] != grid2[i]:
                pos = i + 1
                break
            else:
                continue
        return pos

def human_comp(grid,player):
    pygame.init()      # 硬件准备
    color_white=(255,255,255) # 设置底色
    screen =pygame.display.set_mode([700,700]) #设置窗口大小
    back_image= pygame.image.load("background2.jpg") #导入背景
    pygame.display.set_caption("井字棋") # 设置标题
    X_image = pygame.image.load("X.png") # 导入x图像
    O_image = pygame.image.load('O.png') # 导入o图像
    Draw_image = pygame.image.load('draw.png') # 导入平局图像
    Restart_image = pygame.image.load('Restart1.png') # 导入重新开始游戏的提示图像
    screen.blit(back_image,(0,0)) #显示背景
    pos = None # 位置初始值设置为none
    win_draw_state = False      # True 代表已经有过win或者draw的状态，False代表尚还没有赢或者平局
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #退出事件
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标点击事件
                x,y = pg.position()    # 获得鼠标所在坐标的数值
                if 370 <= x < 599 and 206 <= y < 373 and win_draw_state == False:
                    pos = 0
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(25,87))
                        player = next(player)
                        pos = None
                        if wins('O',grid):    # 判断输赢或者平局
                            screen.blit(O_image,(300,550))
                            win_draw_state = True # 如果有输赢或者平局就给她定义一个状态
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 599 <= x < 838 and 206 <= y < 373 and win_draw_state == False:
                    pos = 1
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(240,87))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 838 <= x < 1069 and 206 <= y < 373 and win_draw_state == False:
                    pos = 2
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(475,87))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 370 <= x < 599 and 373 <= y < 536 and win_draw_state == False:
                    pos = 3
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(25,250))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 599 <= x < 838 and 373 <= y < 536 and win_draw_state == False:
                    pos = 4
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(240,250))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 838 <= x < 1069 and 373 <= y < 536 and win_draw_state == False:
                    pos = 5
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(475,250))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 370 <= x < 599 and 536 <= y < 699 and win_draw_state == False:
                    pos = 6
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(25,420))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 599 <= x < 838 and 536 <= y < 699 and win_draw_state == False:
                    pos = 7
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(240,420))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                elif 838 <= x < 1069 and 536 <= y < 699 and win_draw_state == False:
                    pos = 8
                    if move(grid,pos,player) == []:
                        pos = None
                        continue
                    else:
                        grid = (move(grid,pos,player))
                        screen.blit(O_image,(475,420))
                        player = next(player)
                        pos = None
                        if wins('O',grid):
                            screen.blit(O_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        elif full(grid):
                            screen.blit(Draw_image,(300,550))
                            win_draw_state = True
                            screen.blit(Restart_image,(0,350))
                        else:
                            pygame.display.update()
                            if show_diff_pos(grid) == 1:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 2:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 3:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,87))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 4:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 5:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 6:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,250))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 7:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(25,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 8:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(240,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
                            elif show_diff_pos(grid) == 9:
                                grid = bestmove(grid,'X')
                                screen.blit(X_image,(475,420))
                                player = next(player)
                                if wins('X',grid):
                                    screen.blit(X_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                elif full(grid):
                                    screen.blit(Draw_image,(300,550))
                                    win_draw_state = True
                                    screen.blit(Restart_image,(0,350))
                                else:
                                    continue
            else:
                pygame.display.update()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    human_comp([['','',''],['','',''],['','','']],'O')
                elif keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit() 
                elif keys[pygame.K_l]:
                    human_or_comp()
                else:
                    continue

def main():
    pygame.init()
    color_white= (255,255,255)
    screen =pygame.display.set_mode([700,700])
    back1_image = pygame.image.load('background.jpg')
    pygame.display.set_caption("井字棋")
    screen.blit(back1_image,(0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #退出事件
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pg.position()    #鼠标点击第一块区域进入游戏
                if 493 <= x <= 940 and 460 <= y <= 560:
                    human_or_comp()
                elif 493 <= x <= 940 and 615 <= y <= 715:
                    pygame.quit()   # 点击第二块区域退出游戏
                    sys.exit() 
            else:
                pygame.display.update()
                continue
            
def human_or_comp():
    pygame.init()
    color_white= (255,255,255)
    screen =pygame.display.set_mode([700,700])
    back3_image = pygame.image.load('background3.jpg')
    pygame.display.set_caption('井字棋')
    screen.blit(back3_image,(0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #退出事件
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pg.position()
                if 493 <= x <= 940 and 460 <= y <= 560:
                    human_comp([['','',''],['','',''],['','','']],'O')
                elif 493 <= x <= 940 and 615 <= y <= 715:
                    human_human([['','',''],['','',''],['','','']],'O')
            else:
                pygame.display.update()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_l]:
                    main()
                else:
                    continue

if __name__ == '__main__':
    main()