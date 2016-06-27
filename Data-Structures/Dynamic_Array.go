package main
import "fmt"

var last_ans int
var n int
var seq_list [][]int

func process_query(q_type,x,y int) {
    idx := (x^last_ans)%n
    if q_type == 1 {
        seq_list[idx] = append(seq_list[idx], y)
    } else {
        last_ans = seq_list[idx][y%len(seq_list[idx])]
        fmt.Println(last_ans)
    }
}

func main() {
 //Enter your code here. Read input from STDIN. Print output to STDOUT
    var q int
    fmt.Scanf("%d%d\n", &n, &q)
    seq_list = make([][]int, n)
    for i := range(seq_list) {
        seq_list[i] = []int{}
    }
    last_ans = 0
    q_type,x,y := 0,0,0
    for q > 0 {
        fmt.Scanf("%d%d%d\n", &q_type, &x, &y)
        process_query(q_type, x, y)
        q --
    }
}
