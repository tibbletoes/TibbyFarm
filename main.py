#Tibby farming game 
import items
import sys

class Farmer:
  def __init__(self, currency):
    self.currency = 0

  def AddCurrency(self, amount):
    self.currency += amount

  def SubCurrency(self,amount):
    self.currency -= amount

  def ShowCurrency(self):
    print(f'Balance: {self.currency}')


class Inventory:
  def __init__(self):
    self.inventory = []

  def AddItem(self,item):
    self.inventory.append(item)

  def RemoveItem(self, item):
    self.inventory.pop(item)

  def ShowInventory(self):
    print(self.inventory)

Player = Farmer(500)
PlayerInv = Inventory()


def MainMenu():
  print("\n [1] Farm \n [2] Inventory \n [3] Shop \n [4] Quit")           
  choice = input("What would you like to do? ")
  if choice == "1":
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    items.Shop()
  elif choice == "4":
    print("Whatever, Hater.")
    sys.exit()

MainMenu()