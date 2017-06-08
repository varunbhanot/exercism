
import scala.collection.mutable
import scala.collection.mutable.Map;

class School {
  var db = Map[Int,Seq[String]]()
  var sorted = mutable.SortedMap[Int,Seq[String]]()

  def add(arg: String, arg1: Int) = {
    db.get(arg1) match {
      case None => {
        db.put(arg1, List(arg))
        sorted.put(arg1,List(arg))
      }
      case _ => {
        val newList = db.get(arg1).get.:+(arg)
        db.put(arg1, newList)
        sorted.put(arg1,newList.sorted)
      }
    }


  }


  def grade(arg: Int) = {
    db.getOrElse(arg,Seq())
  }


}