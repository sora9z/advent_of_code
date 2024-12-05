"""
X 자를 이루는 MAS 글자 찾기
정방향 역방향 가능
M.S
.A.
M.S
- 풀이
x 자 모양 확인 조건
1. arr[i][j]+arr[i+1][j+1]+arr[i+2][j+2] = "MAS" or "SAM"
2. arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j] = "MAS" or "SAM"
범위 체크꼭 하기 
"""


import numpy as np


# input = open("./test.txt").read().split("\n")
input = open("./input.txt").read().split("\n")

arr = [list(row) for row in input]


def is_valid(i, j):
    return i+2 < len(input) and j+2 < len(input[0])


def check_x_shape(i, j):
    return input[i][j] + input[i + 1][j + 1] + input[i + 2][j + 2] == "MAS" or input[i][j] + input[i + 1][j + 1] + input[i + 2][j + 2] == "SAM"


def check_x_shape_reverse(i, j):
    return input[i][j + 2] + input[i + 1][j + 1] + input[i + 2][j] == "MAS" or input[i][j + 2] + input[i + 1][j + 1] + input[i + 2][j] == "SAM"


count = 0
for i in range(len(input)):
    for j in range(len(input[0])):
        if is_valid(i, j):
            if check_x_shape(i, j) and check_x_shape_reverse(i, j):
                count += 1

print(count)
