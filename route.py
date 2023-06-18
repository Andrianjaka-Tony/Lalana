from goudron import Goudron

class Route:
  # TODO fields
  # debut
  # fin
  # largeur
  # degat
  # nom
  
  
  # TODO constructors
  def __init__(self, debut, fin, largeur, degat, nom) -> None:
    self.debut = debut
    self.fin = fin
    self.largeur = largeur
    self.degat = degat
    self.nom = nom
    
    
  # TODO functions
  def profondeur(self):
    return self.degat / 10
  
  def distance_metre(self):
    distance_kilometre = self.fin.distance(self.debut)
    distance_metre = distance_kilometre * 1000
    return distance_metre
  
  def surface_route(self):
    distance = self.distance_metre()
    surface = distance * self.largeur
    return surface
  
  def profondeur_metre(self):
    return self.profondeur() / 100
  
  def goudron_necessaire(self):
    surface = self.surface_route()
    profondeur = self.profondeur_metre()
    volume = surface * profondeur
    return volume
  
  def calculer_prix(self):
    volume = self.goudron_necessaire()
    goudron = Goudron()
    prix = volume * goudron.prix_metre_3
    return prix