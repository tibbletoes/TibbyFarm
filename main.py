#Tibby farming game 
import sys

class Farmer:
  def __init__(self):
    self.name = "name"
    self.currency = 500

  def SetName(self):
    self.name = input("What is your name?")

  def AddCurrency(self, amount):
    self.currency += amount

  def SubCurrency(self,amount):
    self.currency -= amount

  def ShowCurrency(self):
    print(f'Balance: {self.currency}')


class Item:
  def __init__(self, name, quantity, price, description):
    self.name = name
    self.quantity = quantity
    self.price = price
    self.description = description


class Inventory:
  def __init__(self):
    self.inventory = []

  def AddItem(self,item):
    self.inventory.append(item)

  def RemoveItem(self, item):
    self.inventory.pop(item)

  def ShowInventory(self):
    print(self.inventory)


def MainMenu():
  print("[1] Farm \n [2] Inventory \n [3] Shop \n [4] Quit")           
  choice = input("What would you like to do? ")
  if choice == "1":
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "4":
    print("Whatever, Hater.")
    sys.exit()

