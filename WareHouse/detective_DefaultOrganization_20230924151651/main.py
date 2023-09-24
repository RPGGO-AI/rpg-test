'''
This is the main file for the RPG game "Sherlock Holmes: Murder Investigation".
The game allows the player to take on the role of Sherlock Holmes and investigate a murder case.
'''
from game_scene import GameScene
def main():
    # Create a new game scene
    game_scene = GameScene()
    # Start the game
    game_scene.start()
if __name__ == "__main__":
    main()