const fs = require("fs");

/**
방법1
- Map을 사용하여 right 리스트에 대하여 값을 키로하고 키의 빈도를 count한 것을 값으로 한다 O(n)
- left를 반복하면서 Map을 사용하여 count를 구하는 동시에 result를 구한다
- 아마 시간 복잡도는 O(n)

방법2 
- 파이썬 내장함수인 bisect_left, bisect_right를 사용한다.
    - 이진탐색이라서 정렬 , 탐색 모두 nlogn이다
- left를 반복문으로 돌면서 범위사이의 count를 구한다
- 이것도 시간복잡도는 O(n) 

방법3 python의 Counter객체 사용

어떤 방법을 사용하든 기본적으로 시간복잡도는 비슷할듯 
*/

const input = fs.readFileSync("./input.txt", "utf-8").split("\n");
// const input = fs.readFileSync("./test.txt", "utf-8").split("\n");

// Count 맵으로  변환
const leftMap = new Map();
const rightMap = new Map();

input.forEach((el) => {
  const [_left, _right] = el.split("   ");
  const left = Number(_left.trim());
  const right = Number(_right.trim());

  leftMap.set(left, (leftMap.get(left) || 0) + 1);
  rightMap.set(right, (rightMap.get(right) || 0) + 1);
});

// result 반환
let sum = 0;
for (const target of leftMap) {
  const [_target, _count] = target;
  sum += _target * _count * (rightMap.get(_target) || 0);
}
console.log(sum);
