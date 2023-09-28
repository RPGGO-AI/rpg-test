'''
Game Scene
This file contains the GameScene class which represents the main game scene and handles the gameplay logic.
'''
from crime_scene import CrimeScene
from suspect import Suspect
from evidence import Evidence
class GameScene:
    def __init__(self):
        # Initialize game variables
        self.crime_scenes = []
        self.suspects = []
        self.evidence = []
        # Create crime scenes
        self.create_crime_scenes()
        # Create suspects
        self.create_suspects()
        # Create evidence
        self.create_evidence()
    def create_crime_scenes(self):
        # Create crime scene objects
        crime_scene1 = CrimeScene("Murder at Baker Street", "A mysterious murder has occurred at Baker Street.")
        crime_scene2 = CrimeScene("The Stolen Diamond", "A valuable diamond has been stolen from a museum.")
        crime_scene3 = CrimeScene("The Missing Heirloom", "A priceless heirloom has gone missing from a mansion.")
        # Add crime scenes to the list
        self.crime_scenes.append(crime_scene1)
        self.crime_scenes.append(crime_scene2)
        self.crime_scenes.append(crime_scene3)
    def create_suspects(self):
        # Create suspect objects
        suspect1 = Suspect("John Smith", "A mysterious man who was seen near the crime scene.")
        suspect2 = Suspect("Emily Johnson", "The victim's close friend with a possible motive.")
        suspect3 = Suspect("Thomas Anderson", "A disgruntled employee of the museum.")
        # Add suspects to the list
        self.suspects.append(suspect1)
        self.suspects.append(suspect2)
        self.suspects.append(suspect3)
    def create_evidence(self):
        # Create evidence objects
        evidence1 = Evidence("Bloody Knife", "A knife found at the crime scene with bloodstains.")
        evidence2 = Evidence("Security Footage", "Footage showing a suspicious person near the museum.")
        evidence3 = Evidence("Fingerprint", "A fingerprint found on the missing heirloom.")
        # Add evidence to the list
        self.evidence.append(evidence1)
        self.evidence.append(evidence2)
        self.evidence.append(evidence3)
    def start(self):
        while True:
            # Display game introduction
            print("Welcome to the Detective RPG Game!")
            print("You are Sherlock Holmes, the world's greatest detective.")
            print("Your goal is to solve various mysteries and crimes.")
            # Display available options
            print("\nAvailable Options:")
            print("1. Investigate Crime Scene")
            print("2. Interrogate Suspects")
            print("3. Analyze Evidence")
            print("4. Quit")
            # Get user input
            choice = input("Enter your choice: ")
            # Process user input
            if choice == "1":
                self.investigate_crime_scene()
            elif choice == "2":
                self.interrogate_suspects()
            elif choice == "3":
                self.analyze_evidence()
            elif choice == "4":
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Please try again.")
    def investigate_crime_scene(self):
        # Display available crime scenes
        print("\nAvailable Crime Scenes:")
        for i, crime_scene in enumerate(self.crime_scenes):
            print(f"{i+1}. {crime_scene.name}")
        # Get user input
        choice = input("Enter the number of the crime scene you want to investigate: ")
        # Process user input
        if choice.isdigit() and int(choice) in range(1, len(self.crime_scenes)+1):
            crime_scene = self.crime_scenes[int(choice)-1]
            print(f"\nInvestigating {crime_scene.name}...")
            print(crime_scene.description)
            print("You found some evidence!")
        else:
            print("Invalid choice. Please try again.")
    def interrogate_suspects(self):
        # Display available suspects
        print("\nAvailable Suspects:")
        for i, suspect in enumerate(self.suspects):
            print(f"{i+1}. {suspect.name}")
        # Get user input
        choice = input("Enter the number of the suspect you want to interrogate: ")
        # Process user input
        if choice.isdigit() and int(choice) in range(1, len(self.suspects)+1):
            suspect = self.suspects[int(choice)-1]
            print(f"\nInterrogating {suspect.name}...")
            print(suspect.description)
            print("You obtained some valuable information!")
        else:
            print("Invalid choice. Please try again.")
    def analyze_evidence(self):
        # Display available evidence
        print("\nAvailable Evidence:")
        for i, evidence in enumerate(self.evidence):
            print(f"{i+1}. {evidence.name}")
        # Get user input
        choice = input("Enter the number of the evidence you want to analyze: ")
        # Process user input
        if choice.isdigit() and int(choice) in range(1, len(self.evidence)+1):
            evidence = self.evidence[int(choice)-1]
            print(f"\nAnalyzing {evidence.name}...")
            print(evidence.description)
            print("You discovered a crucial clue!")
        else:
            print("Invalid choice. Please try again.")