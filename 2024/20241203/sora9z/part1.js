const fs = require("fs");

/**
 * input에 mul(x,y) 를 찾아 곱한 것을 모두 더한 값을 반환
 *
 * regex로 mul(x,y) 를 찾고 계산을 해보자
 */

const input = fs.readFileSync("./input.txt", "utf8");
// const input = fs.readFileSync("./test.txt", "utf8");
const regex = /mul\((\d+),(\d+)\)/g;
const matched = [...input.matchAll(regex)];
let result = 0;
matched.forEach((el) => {
  result += Number(el[1]) * Number(el[2]);
});

console.log(result);
