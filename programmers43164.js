const solution = (tickets) => {
    let answer = [];
    const DFS = (depart, tickets, path) => {
        let newPath = [...path, depart];
        if (tickets.length === 0) {
            answer.push(newPath);
        } else {
            tickets.map((ticket, i) => {
                if (ticket[0] === depart) {
                    let copiedTicket = [...tickets];
                    copiedTicket.splice(i, 1)
                    DFS(ticket[1], copiedTicket, newPath);
                }
            })
        }

    }
    DFS("ICN", tickets, []);
    console.log(answer);
    return answer.sort()[0];
}