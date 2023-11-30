import random

list = []
for number in range(1,101):  
  list.append(number)

num_guess = random.choice(list)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level.lower() == 'easy':
  player_lives = 10
else:
  player_lives = 5

print(f'You have {player_lives} attempts to guess the number')

def count_lives():
  global player_lives
  player_lives -= 1

while player_lives > 0:  
  player_guess = int(input("Make a guess: "))
  if player_guess > num_guess:
    count_lives()
    print(f"Too high, now you have {player_lives} attempt(s)")
  elif player_guess < num_guess:
    count_lives()
    print(f"Too low, now you have {player_lives} attempt(s)")
  elif player_guess == num_guess:
    print("You got it!")
    break
if player_lives == 0:
  print(f'You lost! The number were {num_guess}.')
