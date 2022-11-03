import colorama
import sys
import iridi
from colorama import Fore

QUESTIONS = [
    ("How many continents are there? ", "5", "7", "8"),
    ("What is the biggest country in population?", "Russia", "China", "USA", "Canada"),
    ("What country is the poorest?", "Switzerland", "USA", "Somalia"),
]

iridi.print("Welcome to my quiz, I hope you enjoy :) \n", ["#8A2387", "#E94057", "#F27121"], bold=True)

question = input("How many continents are there? ")
if question == "7": 
  print(f"{Fore.GREEN}Correct!")
  print(f"{Fore.RESET}")
else:
  print(f"{Fore.RED}Incorrect!")
  print(f"{Fore.RESET}")

 
question = input("What is the biggest country in population: ")
if question == "China":
  print(f"{Fore.GREEN}Correct!")
  print(f"{Fore.RESET}")
else:
  print(f"{Fore.RED}Incorrect!")
  print(f"{Fore.RESET}")


question = input("What country is the poorest: ")
if question == "Somalia":
  print(f"{Fore.GREEN}Correct!")
  print(f"{Fore.RESET}")
else:
  print(f"{Fore.RED}Incorrect!")
  sys.exit()

iridi.print("Thank you for playing! Goodbye.", ["#8A2387", "#E94057", "#F27121"], bold=True)
sys.exit()
