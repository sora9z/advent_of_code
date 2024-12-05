const fs = require('fs');

const readInput = (filePath) => {
    const file = fs.readFileSync(filePath, 'utf8');
    const inputs = file.split(/\n/);

    return inputs;
}

const separateLeftRight = (inputs) => {
    const left = inputs.map((value) => Number.parseInt(value.split(/\s+/)[0]));
    const right = inputs.map((value) => Number.parseInt(value.split(/\s+/)[1]));

    left.sort((a, b) => a - b);
    right.sort((a, b) => a - b);
    
    return {
        left, 
        right,
        length: inputs.length,
    };
}

const part1 = () => {
    const inputs = readInput('2024/20241201/camomile.kr/input.txt');
    const separated = separateLeftRight(inputs);

    let result = 0;
    for (let i = 0; i < separated.length; i += 1) {
        result += Math.abs(separated.left[i] - separated.right[i]);
    }

    console.log(`distance between left and right is ${result}`);
    return result;
}

part1();