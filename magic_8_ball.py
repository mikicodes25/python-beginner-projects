import random

responses = ['Yes, definitely', 'Without a doubt', "Don't count on it", 'Ask again later', 'My sources say no', 'Outlook is good', 'Very doubtful', 'Signs point to yes']
repeat = 'y'

while repeat == 'y':

  print('Ask a yes or no question')
  question = input('> ')
  print('You asked: ' + question)
  
  answer = random.choice(responses)
  print(answer)

  repeat = input('Do you want to continue playing? (y for yes, n for no) ')
  print('')

print('Goodbye!')


