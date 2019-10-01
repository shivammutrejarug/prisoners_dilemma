import alwaysCollude, alwaysDefect, titForTat, grudger

strategies = [alwaysCollude,alwaysDefect,titForTat,grudger]

scores = {}
for s in strategies:
  scores[s.name()] = 0

def game(player1,player2,rounds):
  global scores
  p1Score = 0
  p2Score = 0
  p1Move = player1.play('start')
  p2Move = player2.play('start')
  for i in range(rounds):
    if p1Move == 1 and p2Move==1:
      p1Score +=1
      p2Score +=1
      scores[player1.name()] += 1
      scores[player2.name()] += 1
    if p1Move == 1 and  p2Move == 0:
      p2Score +=2
      scores[player2.name()] += 2
    if p1Move == 0 and  p2Move == 1:
      p1Score +=2
      scores[player1.name()] += 2
    prevP1Move = p1Move
    prevP2Move = p2Move
    p1Move = player1.play(prevP2Move)
    p2Move = player2.play(prevP1Move)

  if p1Score>p2Score:
    print(player1.name(),'beats',player2.name(),p1Score,'-',p2Score)
  elif p2Score>p1Score:
    print(player2.name(),'beats',player1.name(),p2Score,'-',p1Score)
  else:
    print('it was a draw',player1.name(),p1Score,player2.name(),p2Score)


def testStrategy(strategy,turns):
  games = 0
  for s in strategies:
    if s != strategy:
      game(strategy,s,turns)
      game(s,strategy,turns)
      games +=2
      print('')
  opScore = scores[strategy.name()]/games
  print('your average score against different opponents was',opScore)
  print('')
  print('So if everybody was doing it')
  for s in strategies:
    scores[s.name()] = 0
  for i in range(turns):
    game(strategy,strategy,turns)
  selfScore = scores[strategy.name()]/(turns*2)
  print('your average score against the same strategy opponents was',selfScore)
  print('your overall average score was',(opScore+selfScore)/2)
