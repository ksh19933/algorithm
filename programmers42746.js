function solution(numbers) {
    numbers = numbers.map((a) => String(a)).sort((a, b) => b + a - (a + b));
    console.log(numbers);
    if(numbers.every(e=> e==='0')){
        return '0';
    }else{
        return numbers.join('');
    }
}