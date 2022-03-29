function solution(n, computers) {
    let answer = 0;
    let stack = [];
    let visited = new Array(n).fill(false);

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            stack.push(i);
            visited[i] = true;
            while (stack.length > 0) {
                let tmp = stack.pop();
                for (let j in computers[tmp]) {
                    if (computers[tmp][j] == 1 && !visited[j]) {
                        stack.push(j);
                        visited[j] = true;
                    }
                }
            }
            answer++
        }

    }

    return answer;
}