case class SpaceAge(seconds: Double) {

  def onEarth = timeConverter(1)
  def onMercury = timeConverter(0.2408467)
  def onVenus = timeConverter(0.61519726)
  def onMars = timeConverter(1.8808158)
  def onUranus = timeConverter(84.016846)
  def onNeptune = timeConverter(164.79132)
  def onSaturn = timeConverter(29.447498)
  def onJupiter = timeConverter(11.862615)

  def yearInSecondsOnEarth = 31557600

  def timeConverter(factor: Double) = {
    BigDecimal((seconds / yearInSecondsOnEarth) / factor).setScale(2, BigDecimal.RoundingMode.HALF_UP).toDouble
  }
}