const fs = require("fs");
/**
 * There are two new instructions you'll need to handle:
 * The do() instruction enables future mul instructions.
 * The don't() instruction disables future mul instructions.
 *
 * Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
 *
 * 일차적으로 don't()~ do() 사이는 제거 or don't() 로 끝나는 것 제거
 * *? 최소 매칭
 * 두 번째로는 part1과 동일하게 해보자
 */

// const input = fs.readFileSync("./test.txt", "utf-8");
const input = fs.readFileSync("./input.txt", "utf-8");
const regexDoFunc = /don't\(\)(.|\n)*?(?:do\(\)|$)/g;
const regex = /mul\((\d+),(\d+)\)/g;
let result = 0;

const removed = input.replace(regexDoFunc, "");
const matched = [...removed.matchAll(regex)];
matched.forEach((el) => {
  result += Number(el[1]) * Number(el[2]);
});

console.log(result);
