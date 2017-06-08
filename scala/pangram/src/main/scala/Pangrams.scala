

object Pangrams {
  def isPangram(input: String): Boolean = {
    input
    .map { x => x.toLower }
    .filter { x => x.isLetter }
    .distinct
    .length == 26

  }
}