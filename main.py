from game import Game

def main():
    game = Game()
    game.is_playing = True
    game.game_loop()

if __name__ == '__main__':
    main()