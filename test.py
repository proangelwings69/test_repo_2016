# testfile

class NBAPlayer:
  species = 'human'
  gender = 'male'
  
  def __init__(self, name):
    self.name = name
  
  def team(city, teamname):
    self.city = city
    self.teamname = teamname
    
  def stats(self, agil, str, stam):
    self.agil = agil
    self.str = str
    self.stam = stam
    
kobe = NBAPlayer('Kobe_Bryant')
kobe.team('Los_Angeles', 'Lakers')
kobe.stats(69, 69, 69)
