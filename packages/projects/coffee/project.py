import iridi
import sys
import colorama
from colorama import Fore

iridi.print("Welcome to the Nijmeh Coffee Shop!\n", ["#8A2387", "#E94057", "#F27121"], bold=True)

MENU = ['Cold Coffee\n',  'Latte\n',  'Pumpkin Spice Latte\n',  'Cappuccino\n']

iridi.print(f"Here is our menu: \n", ["#8A2387", "#E94057", "#F27121"])

print(
  "Cold Coffee"
  "Latte"
  "Pumpkin Spice Latte"
  "Cappuccino\n"
)

menu_length = len(MENU)
print(f"{Fore.GREEN}We currently have", menu_length, "drinks on the menu!\n")
print(f"{Fore.RESET}")



def order_coffee():
  response = input("Would you like to order a coffee? ")
  if response == 'yes':
    customer_order = input("What coffee would you like to order? ") 
    if customer_order == "Cold Coffee":
      print("Ok! That will be 2.50$. You can checkout here!")
    if customer_order == "Cappuccino":
      print("Ok! That will be 3$. You can checkout here!")
    else:
      print("Great choice! You can checkout here!")
    
  else:
    print("Ok! Have a great day\n")
    sys.exit()

order_coffee() 
