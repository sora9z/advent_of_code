"""
아래 두 가지 조건을 만적하는 갯수 찾기
* The levels are either all increasing or all decreasing.
* Any two adjacent levels differ by at least one and at most three.
 반복하면서 조건에 맞는 report의 개수를 찾는다.
"""

input = open("./input.txt", "r").read().strip().split("\n")
# input = open("./test.txt", "r").read().strip().split("\n")
array = list(map(lambda x: list(map(int, x.split(" "))), input))
result = []


for report in array:
    is_increasing = report[0] < report[1]
    is_valid = True
    if is_increasing:
        for i in range(len(report) - 1):
            if (report[i] >= report[i + 1]) or (report[i + 1] - report[i] > 3):
                is_valid = False
                break
    else:
        for i in range(len(report) - 1):
            if (report[i] <= report[i + 1]) or (report[i] - report[i + 1] > 3):
                is_valid = False
                break
    if is_valid:
        result.append(report)

print(len(result))
