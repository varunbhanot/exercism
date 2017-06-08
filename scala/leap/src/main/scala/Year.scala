

case class Year(year: Int) {
  def isLeap(): Boolean = {
    def isDivBy(x: Int, y: Int) = x % y == 0
    (isDivBy(year, 4) && !isDivBy(year, 100)) || isDivBy(year, 400)
  }

}