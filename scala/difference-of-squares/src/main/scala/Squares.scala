

object Squares {
  
  def squareOfSums(in:Int)={
    val range = 1 to in
    Math.pow(range.sum,2)
  }

  def sumOfSquares(arg: Int) = {
    val range = 1 to arg
    range.map(x=>x*x).sum
  }

  def difference(arg: Int) = {
    squareOfSums(arg)-sumOfSquares(arg)
  }
}