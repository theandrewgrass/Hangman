from random_word import RandomWords
from Player import Player

class Game:
    def __init__(self):
        self.word = RandomWords().get_random_word()
        self.player = Player(self.get_blank_word())

    def get_blank_word(self):
        blank_word = ['_' if letter != '-' else '-' for letter in self.word]
        return blank_word

    def play(self):
        while self.player.tries > 0:
            print(self.player)
            guess = self.player.guess_letter()

            if guess in self.player.letters_guessed:
                print("Already guessed.")
                continue
    
            if guess in self.word:
                print("Correct!")
                self.update_player_word(guess)

                if self.player_win():
                    print("Congrats! You won.")
                    break
            else:
                print("wrong")
                self.player.tries -= 1

            self.update_player_letters_guessed(guess)

        print(f'The word was {self.word}!')

    def update_player_word(self, letter_guessed):
        matching_index = [i for i, x in enumerate(self.word) if x == letter_guessed]
        for index in matching_index:
            self.player.word[index] = letter_guessed
		
    def update_player_letters_guessed(self, guess):
        self.player.letters_guessed.append(guess)
	
    def player_win(self):
        if '_' in self.player.word:
            return False
        return True