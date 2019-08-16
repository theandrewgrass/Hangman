class Player:
	def __init__(self, word):
		self.tries = 6
		self.letters_guessed = []
		self.word = word

	def guess_letter(self):
		return input("Guess a letter!\n")
	
	def __str__(self):
		word_string = f'Word: {" ".join(self.word)}'
		guesses_string = f'Guesses: {self.letters_guessed}'
		tries_string = f'Tries left: {self.tries}'
		content_sep = f'{"-"*35}'
		
		return f'{content_sep}\n{word_string}\n{guesses_string}\n{tries_string}\n{content_sep}'