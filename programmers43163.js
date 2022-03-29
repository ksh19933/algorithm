function wordCheck(word, target){
    let change = 0;
    for(let i in word){
        if(word[i] !== target[i]){
            change++;
        }
        if(change > 1){
            return false;
        }
    }
    return true;
}


function solution(begin, target, words) {
    let answer = 50;
    let visited = new Array(words.length).fill(false);
    function dfs(depth, word){
        // console.log(word);
        if(word == target){
            if(depth < answer){
                answer = depth;
            }
            return;
        }
        for(let i = 0; i < words.length; i++){
            let num = 1;
            if(!visited[i]){
                if(wordCheck(word, words[i])){
                    visited[i] = true;
                    dfs(depth+1, words[i]);
                    visited[i] = false;
                }
            }
        }
        return;  
    }
    dfs(0, begin);
    return answer == 50 ? 0 : answer;
}