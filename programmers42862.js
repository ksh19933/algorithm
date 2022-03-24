function solution(n, lost, reserve) {
    let answer = n - lost.length;
    lost.sort((a,b)=>{
        return a-b;
    });
    reserve.sort((a,b)=>{
        return a-b;
    })
    for (let i = 0 ; i < reserve.length; i++ ){            
        if(lost.indexOf(reserve[i]) !== -1){
            answer += 1;
            lost = lost.filter((e)=> e !== reserve[i]);
            reserve.splice(i, 1);
            i--;
        }          
    }

    for (let i = 0 ; i < reserve.length; i++ ){
        if(lost.indexOf(reserve[i] - 1) !== -1){
            answer += 1;
            lost = lost.filter((e)=> e !== reserve[i] - 1);
        } 
        else if(lost.indexOf(reserve[i] + 1) !== -1){
            answer += 1;
            lost = lost.filter((e)=> e !== reserve[i] + 1);
        }
        console.log(lost, reserve);
    }
    return answer;
}