"""
아래 두 가지 조건을 만적하는 갯수 찾기
* The levels are either all increasing or all decreasing.
* Any two adjacent levels differ by at least one and at most three.
* report에서 하나의 원소를 제거했을 때 위의 두 조건을 만족하면 valid한 보고서로 간주한다.
"""
import os

input = open("./input.txt", "r").read().strip().split("\n")
# input = open(os.path.abspath("./test.txt"), "r").read().strip().split("\n")
array = list(map(lambda x: list(map(int, x.split(" "))), input))
result = []


def _is_valid_reposrt(report, is_removed=False):
    def is_valid_diff(a, b):
        diff = abs(b - a)
        return 0 < diff <= 3

    def is_valid_order(report):
        is_increasing = all(report[i] < report[i + 1]
                            for i in range(len(report) - 1))
        is_decreasing = all(report[i] > report[i + 1]
                            for i in range(len(report) - 1))
        return is_increasing or is_decreasing

    if not is_valid_order(report):
        if is_removed:
            return False
        # i번째 요소를 제거하고 다시 확인
        for i in range(len(report)):
            if _is_valid_reposrt(report[:i] + report[i + 1:], True):
                return True
        return False

    for i in range(len(report) - 1):
        if not is_valid_diff(report[i], report[i + 1]):
            if is_removed:
                return False
            # i번째 요소를 제거하고 다시 확인
            for i in range(len(report)):
                if _is_valid_reposrt(report[:i] + report[i + 1:], True):
                    return True
            return False

    return True


for report in array:
    if _is_valid_reposrt(report):
        result.append(report)

print(len(result))  # 318
