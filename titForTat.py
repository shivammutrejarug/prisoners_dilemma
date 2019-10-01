#1 = collude
#0 = defect

def play(opponentMove):
  if opponentMove == 'start':
    return 1
  opponentHistory = []
  opponentHistory.append(opponentMove)
  if opponentHistory:
    return opponentHistory[-1]
  else:
    return 1
  return 0

def name():
  return 'titForTat'

