object Raindrops {

  def convert(n: Int): String =  {
   val output :StringBuilder = new StringBuilder
    if(n%3==0){
      output.append("Pling")
    }
    if(n%5==0){
      output.append("Plang")
    }
    if(n%7==0){
      output.append("Plong")
    }
    if(output.isEmpty){
      output.append(n.toString)
    }
    output.toString
  }

}

