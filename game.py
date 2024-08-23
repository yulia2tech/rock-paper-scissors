# import rendom module for the computer's pick
import random


# create a class
# class attributes computer_pick, user_pick, result ('win', 'lose', 'draw')
class Game:
    def __init__(self):
        # call get the get_computer_pick() method
        self.computer_pick = self.get_computer_pick()

        # call get the get_user_pick method
        self.user_pick = self.get_user_pick()

        # call get the get_result() method 
        self.result = self.get_result()

    def get_computer_pick(self):
        # get a random number among 1, 2 and 3
        random_number = random.randint(1, 3)

        # assign options by creating a dictionary to store key/value pairs
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}

        # return the value present at random number
        return options[random_number]
    
    def get_user_pick(self):
        # make user input a valid string
        while True:
            user_pick = input('Enter rock/paper/scissors: ')
            
            # return value and convert it to lower case
            user_pick = user_pick.lower()

            # if valid break the loop
            if user_pick in ('rock', 'paper', 'scissors'):
                break
            else:
                print('Wrong input!')
        
        return user_pick
    
    def get_result(self):
        # condition for draw
        if self.computer_pick == self.user_pick:
            return 'draw'
        
        # condition for the user to win
        elif self.user_pick == 'paper' and self.computer_pick == 'rock':
            return 'win'
        elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
            return 'win'
        elif self.user_pick == 'scissors' and self.computer_pick == 'paper':
            return 'win'
        
        #else users lose
        else:
            return 'lose'
        
    def print_result(self):
        print(f"Computer's pick: {self.computer_pick}")
        print(f"Your pick: {self.user_pick}")
        print(f"You {self.result}")
        
#ask if user wants to play again
while True:
    # create an object of the Game class
    game = Game()
    game.print_result()

    play_again = input('Do you want to play again? (y/n): ')
    play_again = play_again.lower()
    
    if play_again == 'y' or play_again == 'yes':
        continue
        
    else:
        print('Thanks for playing!')
        break 