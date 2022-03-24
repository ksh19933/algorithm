function solution(jobs) {
    let answer = 0;
    let priorityQueue = [];
    jobs.sort((a, b) => {
        return a[0] - b[0];
    })
    let j = 0;
    let time = 0;
    while (j < jobs.length || priorityQueue.length !== 0) {
        if (jobs.length > j && time >= jobs[j][0]) {
            priorityQueue.push(jobs[j++]);
            priorityQueue.sort((a, b) => {
                return a[1] - b[1];
            })
            continue;
        }

        if (priorityQueue.length == 0) {
            time = jobs[j][0];
        } else {
            const tmp = priorityQueue.shift();
            answer += time + tmp[1] - tmp[0];
            time += tmp[1];
        }
    }
    return parseInt(answer / jobs.length);
}