function solution(priorities, location) {
    let answer = 0;
    let max = 0;
    let cnt = 0;

    while(priorities.length > 0){
        let tmp = priorities.shift();
        if(priorities.filter((i)=> i > tmp).length > 0){
            priorities.push(tmp);
        }else{
            cnt++
            if (location == 0){
                return cnt
            }
        }
        location--
        if(location == -1){
            location = priorities.length - 1;
        }
    }
}

console.log(solution([1, 1, 9, 1, 1, 1], 0));