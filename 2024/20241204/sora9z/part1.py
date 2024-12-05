import re
import numpy as np

"""
https://adventofcode.com/2024/day/4
 *
 * 문제 설명
 * 가로,세로,대각선,역방향 에서 xmax 단어를 찾고 개수 리턴
 *
 * 1. 가로 순방향, 역방향 찾기
 *    - regex : /xmax/g
 * 2. 세로 순방향, 역방향 찾기
 *    - 배열을 행렬 대치하여 찾기
 *    - regex : /xmax/g
 * 3. 대각선 순방향, 역방향 찾기
 * 4. 모든 결과 더하기
 *
 * 가로방향 regex로 쉽게 찾을 수 있다.
 * 세로방향은 전치행렬로 변환하여 가로방향과 비슷하게 찾는다
 * 대각선의 경우 방법은
 * 1. 대각선으로 순회하면서 찾기 -> 복잡하긴 할 것 같다
 * 2. 대각선을 하나의 row로 변환하면 가로,세로 방향과 같이 쉽게 찾을 수 있을 것 같다
 * - 찾아보니 대각선을 하나의 row로 변환하는 것이 수학적으로 이것을 대각선 순회(Diagonal Traversal) 또는 대각선 추출(Diagonal Extraction) 이라고 한다고 한다
 *
 * 즉 xmax를 찾는 것은 regex로 하고
 * 각 행렬들을 변환하여 가로방향으로 탐색 가능하도록 만든다
"""

input = open("./test.txt").read().split("\n")
# input = open("./input.txt").read().split("\n")


def get_all_diagonals(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    diagonals = []

    # 왼쪽 구석부터 시작하여 오른쪽 구석까지 대각선 추출
    for i in range(-(rows - 1), cols):
        diagonals.append(np.diagonal(matrix, offset=i))

    return [''.join(row) for row in diagonals]


def count_matching_words(array):
    count = 0
    for word in array:
        if re.search(r'xmas', word, re.IGNORECASE):
            count += 1
        if re.search(r'samx', word, re.IGNORECASE):
            count += 1
    return count


count = 0
# 1. 가로방향 + 가로 역방향 순회
count += count_matching_words(input)
# 2. 세로방향 + 세로 역방향 순회
matrix = [list(row) for row in input]
vertical_arr = [''.join(row) for row in np.transpose(matrix)]
count += count_matching_words(vertical_arr)
# # 3. 왼-오 대각선방향 + 대각선 역방향 순회
diagonals = get_all_diagonals(matrix)
count += count_matching_words(diagonals)
# # 4. 오-왼 대각선방향 + 대각선 역방향 순회
matrix = np.fliplr(matrix)
diagonals = get_all_diagonals(matrix)
count += count_matching_words(diagonals)
print(count)
