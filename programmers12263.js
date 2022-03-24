function solution(N, number) {
    const use = Array.from(new Array(9), () => new Set());
  
    if (N === number) {
      return 1;
    } else {
      use.forEach((element, index) => {
        if (index !== 0) element.add(Number(String(N).repeat(index)));
      });
      console.log(use);
      for(let i = 1; i < 9; i++){
          for(let j = 1; j<i; j++){
              for (subset1 of use[j]){
                  for (subset2 of use[i-j]){
                      use[i].add(subset1 + subset2);
                      use[i].add(subset1 - subset2);
                      use[i].add(subset1 * subset2);
                      use[i].add(Math.floor(subset1/subset2));
                  }
              }
          }
          if(use[i].has(number)){
              return i;
          }
      }
      return -1;
    }
  }