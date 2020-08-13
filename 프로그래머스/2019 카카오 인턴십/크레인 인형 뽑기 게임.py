def solution(board, moves):
    lst = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                if lst and lst[-1] == board[j][i - 1]:
                    del lst[-1]
                    cnt += 2
                else:
                    lst.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
    return cnt


Board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
Moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(Board, Moves))
