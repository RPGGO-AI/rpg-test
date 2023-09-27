'''
This is the main file of the RPG game "Sherlock Holmes: Murder Investigation". It serves as the entry point for the game and contains the game loop.
'''
from game_scene import GameScene
def main():
    # Create an instance of the game scene
    game_scene = GameScene()
    # Start the game loop
    while True:
        game_scene.update()
        game_scene.render()
if __name__ == "__main__":
    main()