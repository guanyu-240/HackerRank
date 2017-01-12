Object Introduction {

  // First FP
  // https://www.hackerrank.com/challenges/fp-solve-me-first
  def printsum(a:Int, b:Int) = {println(a+b)}
  
  // List Replication
  // https://www.hackerrank.com/challenges/fp-list-replication
  def list_replication(num:Int,arr:List[Int]):List[Int] = arr.flatMap(Array.fill(num)(_))
  
  // Filter Array
  // https://www.hackerrank.com/challenges/fp-filter-array
  def filter_arr(delim:Int,arr:List[Int]):List[Int] = (for (x <- arr if x < delim) yield x)
   
  // Filter Positions in a List
  // https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list
  def filter_pos(arr:List[Int]):List[Int] = (for ((x,i) <- arr.zipWithIndex if i%2 == 1) yield x)
  
  // Sum of odd elements
  // https://www.hackerrank.com/challenges/fp-sum-of-odd-elements
  def sum_odd(arr:List[Int]):Int = arr.filter(_%2 != 0).sum
  
  // List length
  // https://www.hackerrank.com/challenges/fp-list-length?h_r=next-challenge&h_v=zen
  def list_length(l:List[Int]):Int = l match {
    case Nil => 0
    case head::tail => 1 + f(tail)
  }
  
  // Reverse a list
  // https://www.hackerrank.com/challenges/fp-reverse-a-list
  def reverse(arr:List[Int]):List[Int] = {
    // recursively reverse and store res to acc
    def reverse_helper(arr:List[Int], acc:List[Int]):List[Int] = arr match {
      case Nil => acc
      case head::tail => reverse_helper(tail, head::acc)
    }
    reverse_helper(arr, Nil)
  }
}
