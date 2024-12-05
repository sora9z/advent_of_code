import fs from 'fs';
import { BaseSolvePuzzle } from '../../BaseSolvePuzzle';

export class Puzzle_P20241201 implements BaseSolvePuzzle {
    constructor() {}

    _readInput = (filePath: string) => {
        const file = fs.readFileSync(filePath, 'utf8');
        const inputs = file.split(/\n/);
    
        return inputs;
    }

    _separateLeftRight = (inputs: Array<string>) => {
        const left: Array<number> = inputs.map((value) => Number.parseInt(value.split(/\s+/)[0]));
        const right: Array<number> = inputs.map((value) => Number.parseInt(value.split(/\s+/)[1]));
    
        left.sort((a, b) => a - b);
        right.sort((a, b) => a - b);
        
        return {
            left, 
            right,
            length: inputs.length,
        };
    }

    solvePuzzle() {
        const inputs = this._readInput('2024/20241201/camomile.kr/input.txt');
        const separated = this._separateLeftRight(inputs);

        let result = 0;
        for (let i = 0; i < separated.length; i += 1) {
            result += Math.abs(separated.left[i] - separated.right[i]);
        }

        console.log(`distance between left and right is ${result}`);
        return result;
    }
}
