from art import logo
from art import vs
from game_data import data
from replit import clear
import random

print(logo)

game_over = False

def format_data(account):
  """Formats data into readable format"""
  celebrity_name = account['name']
  celebrity_profession = account['description']
  celebrity_country = account['country']

  return f"{celebrity_name}, a {celebrity_profession.lower()} from {celebrity_country}."

def compare_choices(guess, first_followers, second_followers):
  """Checks to see if user answer is correct."""
  if first_followers > second_followers:
    return guess == "a"
  else:
    return guess == "b"

score = 0

second_celebrity = random.choice(data)

while not game_over:
  first_celebrity = second_celebrity
  second_celebrity = random.choice(data)
  while first_celebrity == second_celebrity:
    second_celebrity = random.choice(data)

  print(f"Compare A: {format_data(first_celebrity)}")
  print(vs)
  print(f"Compare B: {format_data(second_celebrity)}")

  choice = input("Who has more followers? Choose A or B: ").lower()

  first_celebrity_followers = first_celebrity['follower_count']

  second_celebrity_followers = second_celebrity['follower_count']

  is_correct = compare_choices(choice, first_celebrity_followers, second_celebrity_followers)

  clear()
  print(logo)

  if is_correct:
    game_over = False
    score += 1
    print("You're right!")
    print(f"Your score so far: {score}")
  else:
    game_over = True
    print(f"Sorry, you lose. Final score: {score}")