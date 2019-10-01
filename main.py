import simulation, interactive_game, alwaysCollude, alwaysDefect, titForTat, grudger

choices = {'1-alwaysCollude', '2-alwaysDefect', '3-titForTat', '4-grudger'}

strategies = {1:alwaysCollude,2:alwaysDefect,3:titForTat,4:grudger}

print('Here are your game options')
print('press 1 to test your AI strategy against all other AI strategies')
print('press 2 to play against an AI strategy of your choice ')
choice = int(input())

if choice == 1:
  print('here are the strategies, choose one')
  print(choices)
  num = int(input('choose a strategy via number'))
  strategy = strategies[num]
  simulation.testStrategy(strategy,20)


if choice == 2:
  print('who do you want to play against')
  print(choices)
  num = int(input('choose a strategy via number'))
  strategy = strategies[num]
  rounds = int(input('how many rounds do you want to play:'))
  interactive_game.play(strategy,rounds)
