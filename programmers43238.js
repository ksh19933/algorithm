function solution(n, times) {
    times.sort((a,b)=> a-b);
    let answer = 0;
    let left = 0;
    let right = times[times.length-1] * n;
    let mid = Math.floor((left+right)/2);
    while(left <= right){
        let count = 0;
        for(let i in times){
            count += Math.floor(mid/times[i]);
        }
        if(count >= n){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
        mid = Math.floor((left+right)/2)
    }
    return left;
}