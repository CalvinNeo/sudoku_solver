#coding:utf8

def read_problem(src):
    # lines = src.strip('\n').split(';')
    # board = [ map(lambda s: int(s) ,lsrc) for lsrc in lines]
    board = map(lambda s: int(s) ,src.strip('\n').replace(';',''))
    return board

def lc_index(line, col):
    return line * 9 + col

def index_lc(index):
    return int(index / 9), index % 9

def get_box(index):
    '''
        box_id:
        0|1|2
        3|4|5
        6|7|8
    '''
    box_left_top = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    l, c = index_lc(index)
    ldelta = int(l / 3) * 3
    cdelta = int(c / 3) 
    box_id = ldelta + cdelta
    start_id =  box_left_top[box_id]
    return [start_id, start_id+1, start_id+2, start_id+9, start_id+10, start_id+11, start_id+18, start_id+19, start_id+20]

def get_line(index):
    start_id = int(index / 9) * 9
    return map(lambda x: x+start_id, range(9))

def get_col(index):
    start_id = index % 9
    return map(lambda x: x*9+start_id, range(9))

def get_value(index_list, board):
    return map(lambda x: board[x], index_list)

def possible_ans(index, board):
    box = get_value(get_box(index), board)
    line = get_value(get_line(index), board)
    col = get_value(get_col(index), board)
    return list(set([1,2,3,4,5,6,7,8,9]) - set(filter(lambda x: x!=0, set(box+col+line))))

def back_solver(board):
    def solve_iter(board, blank):
        if len(blank) > 0:
            pa = possible_ans(blank[0], list(board))
            if len(pa) > 0:
                for a in pa:
                    board[blank[0]] = a
                    solve_iter(list(board), blank[1:])
                    board[blank[0]] = 0
            else:
                return
        else:
            print board

    blank = []
    for i, vi in zip(range(81), board):
        if vi == 0:
            blank.append(i)
    if len(blank) > 0:
        solve_iter(list(board), blank)

if __name__ == '__main__':
    # print read_problem("356148792;917326485;824597361;692453817;785619243;143782956;479265138;261834579;538971624")
    # print get_box(79)
    # print list(set([1,2,3,4,5]) - set([3,4,5]))
    back_solver(read_problem("006008092;000020000;004000301;002050010;780009000;140002006;470060108;261000570;030000000"))
