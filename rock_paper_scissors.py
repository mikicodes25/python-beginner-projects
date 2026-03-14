#RPS on my own
import random

wins = 0
losses = 0
ties = 0
replay = 'Y'
choices = ['R', 'P', 'S']

print("Let's play Rock, Paper, Scissors!")
print('Type R for rock, P for paper, S for scissors')

while replay == 'Y':
  player_choice = input('Make your choice: ').upper()
  computer_choice = random.choice(choices)

  print('You chose:', player_choice, 'I chose:', computer_choice)
  if player_choice == 'R' and computer_choice == 'R':
    ties += 1
    print("It's a tie!")
  elif player_choice == 'R' and computer_choice == 'P':
    losses += 1
    print('You lose!')
  elif player_choice == 'R' and computer_choice == 'S':
    wins += 1
    print('You win!')
  elif player_choice == 'P' and computer_choice == 'P':
    ties += 1
    print("It's a tie!")
  elif player_choice == 'P' and computer_choice == 'S':
    losses += 1
    print('You lose!')
  elif player_choice == 'P' and computer_choice == 'R':
    wins += 1
    print('You win!')
  elif player_choice == 'S' and computer_choice == 'S':
    ties += 1
    print("It's a tie!")
  elif player_choice == 'S' and computer_choice == 'R':
    losses += 1
    print('You lose!')
  elif player_choice == 'S' and computer_choice == 'P':
    wins += 1
    print('You win!')

  tracker = f'Wins: {wins} Losses: {losses} Ties: {ties}'
  print(tracker)
    
  replay = input('Do you want to keep playing? (Y for yes, N for no)')

print('Here are the final results:')
print(tracker)
if wins > losses:
  print('Overall, you won! Great job!')
elif losses > wins:
  print('Overall, you lost! Better luck next time.')
elif wins == losses:
  print('Overall, you tied!')
