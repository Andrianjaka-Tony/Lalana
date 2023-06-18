class Point:
  # TODO fields
  # valeur_kilometre
  # latitude
  # longitude
  
  
  # TODO constructors
  def __init__(self, valeur_kilometre = 0, latitude = "null", longitude = "null"):
    self.valeur_kilometre = valeur_kilometre
    self.latitude = latitude
    self.longitude = longitude
  
  
  # TODO functions
  def distance(self, otherPoint):
    return self.valeur_kilometre - otherPoint.valeur_kilometre  