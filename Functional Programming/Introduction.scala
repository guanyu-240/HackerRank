Object Introduction {

  // First FP
  // https://www.hackerrank.com/challenges/fp-solve-me-first
  def printsum(a:Int, b:Int) = {println(a+b)}
  
  // List Replication
  // https://www.hackerrank.com/challenges/fp-list-replication
  def f(num:Int,arr:List[Int]):List[Int] = arr.flatMap(Array.fill(num)(_))
  
  // Filter Array
  // https://www.hackerrank.com/challenges/fp-filter-array
  def f(delim:Int,arr:List[Int]):List[Int] = (for (x <- arr if x < delim) yield x)
   
  // Filter Positions in a List
  // https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list
  def f(arr:List[Int]):List[Int] = (for ((x,i) <- arr.zipWithIndex if i%2 == 1) yield x)
}
