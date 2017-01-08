Object Recursion{
  // Compute GCD
  //https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd
  def gcd(x: Int, y: Int): Int =
   {
       if (x <= 0 || y <= 0) 0
       else if (x >= y) (if (x%y == 0) y else gcd(y, x%y))
       else (if (y%x == 0) x else gcd(x, y%x))
   }
   
   // Fibonacci
   // https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---fibonacci-numbers
   def fibonacci(x:Int):Int = {
       x match {
           case y if y <= 0 => 0
           case 1 => 0
           case 2 => 1
           case _ => fibonacci(x-1) + fibonacci(x-2)
       }
     }
}
