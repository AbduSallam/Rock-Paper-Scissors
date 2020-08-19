import random

rps = ['ROCK', 'PAPER', 'SCISSORS']

game_over = False
user_lives = 5
computer_lives = 5

print('These are the rules of the game:')
print('You and the computer both start with 5 lives')
print('If you lose a round, you lose a life')
print('If the computer loses a round, the computer loses a life')
print('Type \'end\' at anytime to end the game')

while not game_over and user_lives > 0 and computer_lives > 0:
  user_input = input('Would you like to choose rock, paper, or scissors? ').upper()
  computer_input = random.choice(rps)

  if user_input == 'END':
    game_over = True
    break

  elif user_input in rps:
    if (user_input == 'ROCK' and computer_input == 'PAPER') or (user_input == 'PAPER' and computer_input == 'SCISSORS') or (user_input == 'SCISSORS' and computer_input == 'ROCK'):
      user_lives -= 1
      print('The Computer won this round')
    elif (user_input == 'PAPER' and computer_input == 'PAPER') or (user_input == 'ROCK' and computer_input == 'ROCK') or (user_input == 'PAPER' and computer_input == 'PAPER'):
      print('You both tied')
    elif (user_input == 'SCISSORS' and computer_input == 'PAPER') or (user_input == 'ROCK' and computer_input == 'SCISSORS') or (user_input == 'PAPER' and computer_input == 'ROCK'):
      computer_lives -= 1
      print('You won this round')
    print (f'The computer chose {computer_input}')
    print (f'You chose {user_input}')
    print (f'You have {user_lives} lives remaining')
    print (f'The computer has {computer_lives} lives remaining')
  

  else:
    print('Sorry, what you entered is invalid')  

if user_lives == 0:
  print('Unfortunately the computer has won the game, better luck next time')
  game_over = True
  
elif computer_lives == 0:
  print('Congratulations, you have won the game!')
  game_over = True  