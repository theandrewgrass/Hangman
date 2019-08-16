from Game import Game

def main():
	while True:
		game = Game()
		game.play()
		
		if input("Play again?\n") != 'y':
			break

if __name__ == "__main__":
	main()