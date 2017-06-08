object SumOfMultiples {
  def sumOfMultiples(factors: Set[Int], limit: Int): Int = {
    val r = 0 until limit   
    r.filter { x => factors.filter { y => x % y == 0 }.size > 0 }.sum
  }
}

