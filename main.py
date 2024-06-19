#Tibby farming game 
from shop import Shop
import sys


def MainMenu():
  print("\n [1] Farm \n [2] Inventory \n [3] Shop \n [4] Quit")           
  choice = input("What would you like to do? ")
  if choice == "1":
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    Shop()
  elif choice == "4":
    print("Whatever, Hater.")
    sys.exit()

MainMenu()