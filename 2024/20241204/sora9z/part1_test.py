import numpy as np

input = open("./test.txt").read().split("\n")

# 2차원 너파이 행렬로 변환한다
matrix = [list(row) for row in input]

test_matrix = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]


def get_all_diagonals(matrix, reverse=False):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    diagonals = []

    # 왼쪽 구석부터 시작하여 오른쪽 구석까지 대각선 추출
    for i in range(-(rows - 1), cols):
        diagonals.append(np.diagonal(matrix, offset=i))

    if reverse:
        diagonals = [''.join(row[::-1]) for row in diagonals]

    return [''.join(row) for row in diagonals]


# 문자열로 변환
# matrix_to_str = [''.join(row) for row in get_all_diagonals(matrix)]
# 왼쪽 위에서 오른쪽 아래로 대각선
print(get_all_diagonals(test_matrix))
# 오른쪽 아래에서 왼쪽 위로 대각선
print(get_all_diagonals(test_matrix, reverse=True))
# 오른쪽 위에서 왼쪽 아래로 대각선
# fliplr : 행렬을 좌우로 뒤집는다
print(get_all_diagonals(np.fliplr(test_matrix)))
# 오른쪽 아래에서 왼쪽 위로 대각선
print(get_all_diagonals(np.fliplr(test_matrix), reverse=True))
