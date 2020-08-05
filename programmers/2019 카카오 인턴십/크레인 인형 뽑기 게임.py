def solution(board, moves):
    lst = []
    cnt = 0
    for i in moves:  # 각 moves 에서
        for j in range(len(board)):  # board를 위에부터 훑음
            if board[j][i - 1] != 0:  # board에 숫자가 나타나면
                if lst and lst[-1] == board[j][i - 1]:  # lst 배열이 비어있지 않고 lst 배열의 제일 위에 있는 숫자가 뽑은 숫자와 같으면
                    del lst[-1]  # 제일 위에 있는 숫자를 제거하고
                    cnt += 2  # 인형을 두개 터트렸으므로 cnt에 2를 추가
                else:
                    lst.append(board[j][i - 1])  # lst 배열의 제일 위에 있는 숫자와 같지않으면 lst 배열에 추가시킴
                board[j][i - 1] = 0  # 뽑은 숫자의 자리를 0으로 바꿈
                break  # 숫자를 뽑았으므로 다음 move로 넘어감
    return cnt  # 총 터트린 인형의 개수를 리턴


Board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
Moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(Board, Moves))
