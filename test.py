"""This executable file aims to calculate the rate of success. 
The output is a tuple, the first element represents the cases of success,
the second element represents the cases of draw"""
import Tictactoe as ttt
def comp_gametree(grid,player):
    if ttt.full(grid):
        possible_moves = []
    elif ttt.won(grid):
        possible_moves = []
    else:
        if player == 'O':
            possible_moves = ttt.moves(grid,player)
        elif player == 'X':
            possible_moves = [ttt.move(grid,(ttt.show_diff_pos(grid))-1,player)]
    leave = list(map(lambda x:comp_gametree(x,ttt.next(player)),possible_moves))
    result = [grid] + [leave]
    return result

def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res

def win_draw_counter(grid,player):
    win_counter = 0
    draw_counter = 0
    ct = comp_gametree(grid,player)
    flatten_ct = ttt.chop(3,(ttt.chop(3,flat(ct))))
    for i in range(len(flatten_ct)):
        if ttt.won(flatten_ct[i]):
            win_counter += 1
        elif ttt.full(flatten_ct[i]):
            draw_counter += 1
    return (win_counter,draw_counter)

if __name__ == '__main__':
    print(win_draw_counter([['','',''],['','',''],['','','']],'O'))