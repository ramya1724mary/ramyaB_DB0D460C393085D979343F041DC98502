class player:
  def player(self):
        print("The player is playing cricket")

class Batsman(player):
  def play(self):
        print("Batsman is batting.")
class Bowler(player):
  def play(self):
        print("Bowler is bowling. ")

Batsman=Batsman()
Bowler=Bowler()

Batsman.play()
Bowler.play()