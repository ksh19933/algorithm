function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let queue = [[0,0]];
    let weightSum = 0;
    while(queue.length > 0 || truck_weights.length > 0  ){
        if(queue[0][1] === time){
            weightSum -= queue.shift()[0];
        }
        if(weightSum + truck_weights[0] <= weight){
            weightSum += truck_weights[0];
            queue.push([truck_weights.shift(), time+bridge_length]);
        }else{
            if(queue[0]) time = queue[0][1] -1;
        }
        time++;
    }
    return time;
}