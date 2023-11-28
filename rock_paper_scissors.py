rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors_list = list((rock, paper, scissors))


def evaluate_game(player_choice, computer_choice):
    winner = 'You lose.'
    player_wins = ((player_choice == 0 and computer_choice == 2)
                   or (player_choice == 1 and computer_choice == 0)
                   or (player_choice == 2 and computer_choice == 1))
    tie = player_choice == computer_choice
    if player_wins:
        winner = 'You win.'
    elif tie:
        winner = 'It\'s a tie.'
    return winner
