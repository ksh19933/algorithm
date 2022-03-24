function solution(answers) {
    let answer = [];
    let scores = [0, 0, 0];
    const stu2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] == (i % 5) + 1) {
            scores[0] += 1;
        }
        // 1,3,5,7,9,11
        // (i // 2) % 4 
        if (answers[i] == stu2[i % 8]) {
            scores[1] += 1;
        }

        if (answers[i] == stu3[i % 10]) {
            scores[2] += 1;
        }
    }
    const max_num = Math.max(...scores);
    for (let i = 0; i < 3; i++) {
        if (scores[i] == max_num) {
            answer.push(i + 1);
        }
    }
    return answer;
}