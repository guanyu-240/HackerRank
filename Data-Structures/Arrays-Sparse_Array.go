package main
import "fmt"

func AddToDict(dict *map[string]int, s string) {
    (*dict)[s]++;
}

func main() {
 //Enter your code here. Read input from STDIN. Print output to STDOUT
    dict := make(map[string]int)
    var n int
    var i int
    var s string
    fmt.Scanf("%d\n", &n)
    for i = 0; i < n; i++ {
        fmt.Scanf("%s\n", &s)
        AddToDict(&dict, s)
    }
    var q int
    fmt.Scanf("%d\n", &q)
    for i = 0; i < q; i++ {
        fmt.Scanf("%s\n", &s)
        fmt.Println(dict[s])
    }
}
