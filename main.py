import rock_paper_scissors
import random

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors'))
computer_choice = int(round(random.random() * 2))
result = rock_paper_scissors.evaluate_game(player_choice, computer_choice)

print(rock_paper_scissors.rock_paper_scissors_list[player_choice])
print(f'Computer chose:\n{rock_paper_scissors.rock_paper_scissors_list[computer_choice]}')
print(result)
