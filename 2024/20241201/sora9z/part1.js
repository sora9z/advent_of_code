const fs = require("fs");
/**
 * - 왼쪽을 오름차순으로 정렬하고 오른쪽도 오름차순으로 정렬한다.
 * - 왼쪽과 오른쪽의 차이의 절댓값을 구한다.
 * - 차이의 합을 구한다
 *
 * - 시간복잡도는 O(NlogN)이다.
 * - 이유는 각각 정렬을 하는데 js의 sort알고리즘은 복잡도가 O(NlogN)이다.
 * - 차이를 구하는데 O(N)
 * - O(NlogN) + O(N) = O(NlogN)
 *
 * 고려했던 부분
 * 최소힙을 사용하면 정렬을 별도로 안해도 되긴 하지만 복잡도가 비슷하여 sort로 구현
 */

const input = fs.readFileSync("./input.txt", "utf-8").split("\n");
// const input = fs.readFileSync("./test.txt", "utf-8").split("\n");

const left = [];
const right = [];

input.forEach((el) => {
  const [_left, _right] = el.split("   ");
  left.push(Number(_left.trim()));
  right.push(Number(_right.trim()));
});

left.sort((a, b) => a - b);
right.sort((a, b) => a - b);

// 차이 계산
let sum = 0;
for (let i = 0; i < left.length; i++) {
  sum += Math.abs(left[i] - right[i]);
}
console.log(sum); // 2769675
