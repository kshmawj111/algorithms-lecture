def print_2d(a, path=False):
    if not path:
        for x in a:
            print('[', end='')
            for y in x:
                print('{0:3}'.format(y), end=', ')

            print(']', end='\n')

    else:
        t = ['↖', '↑', '←']

        for x in a:
            print('[', end='')
            for y in x:
                print('{0:2}'.format(t[y]), end=', ')

            print(']', end='\n')

def find_path(path, row_string, col_string):
    r, c = len(path)-1, len(path[0])-1
    DIAG, UP, LEFT = 0,1,2
    row_result, col_result = '', ''

    # LEFT -> M은 그대로, N은 '-'
    # UP -> M은 '-', N은 그대로
    # DIAG -> 둘 다 출력
    while r > 0 or c > 0:
        next_move = path[r][c]

        if next_move == UP:
            row_result += row_string[r]
            col_result += '-'
            r -= 1

        elif next_move == LEFT:
            row_result += '-'
            col_result += col_string[c]
            c -= 1

        elif next_move == DIAG:
            row_result += row_string[r]
            col_result += col_string[c]
            r-=1
            c-=1


    return row_result, col_result




def solution(col_string, row_string):
    COL, ROW = len(col_string), len(row_string) # a: col, b: row -> COL: col, ROW: row
    dp = [[0]*COL for _ in range(ROW)]
    path = [[0]*COL for _ in range(ROW)]
    GAP, MISS, MATCH = -1, 0, 1
    DIAG, UP, LEFT = 0,1,2

    result = ''

    for r in range(ROW):
        dp[r][0] = GAP*r
        path[r][0] = UP

    for c in range(COL):
        dp[0][c] = GAP*c
        path[0][c] = LEFT

    for r in range(1, ROW):
        for c in range(1, COL):

            if col_string[c] == row_string[r]:
                t = [dp[r-1][c-1]+MATCH, dp[r-1][c]+GAP, dp[r][c-1]+GAP] # from diag, from up, from left
                dp[r][c] = max(t)
                path[r][c] = t.index(dp[r][c])

            else:
                t = [dp[r - 1][c - 1] + MISS, dp[r - 1][c] + GAP, dp[r][c - 1] + GAP]
                dp[r][c] = max(t)
                path[r][c] = t.index(dp[r][c])

    print_2d(dp)
    print('$'*50)
    print_2d(path, True)

    row_r, col_r = find_path(path, row_string, col_string)

    return row_r[::-1], col_r[::-1]


if __name__ == '__main__':
    a = '-BANDMASTERS'
    b = '-TWINSET'
    print(solution(a, b))