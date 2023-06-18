from .game import Game

def main():
    game = Game()

    while game.isRunning:
        game.update()
        game.handle_event()
        game.render()

    game.clean()

if __name__ =="__main__":
    main()



