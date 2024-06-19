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

def Shop(Item):
  print("Welcome! What can I do for ya'?")
  choice = input("\n [1] Buy \n [2] Sell \n [3] Leave")
  if choice == "1":
    print(f'[1] {Item.WheatSeeds}')
    print(f'[2] {Item.BlueberrySeeds}')
    print(f'[3] {Item.HyacinthSeeds}')
    print(f'[4] {Item.RaspberrySeeds}')
    print(f'[5] {Item.StrawberrySeeds}')
    print(f'[6] {Item.WatermelonSeeds}')
    print(f'[7] {Item.PearSapling}')
    print(f'[8] {Item.CherrySapling}')
    print(f'[9] {Item.LemonSapling}')
    print("[10] Leave")
    choice = input("What would you like to buy?")
    if choice == "1" and Player.currency >= Item.WheatSeeds.price:
        Player.SubCurrency(Item.WheatSeeds.price)
        PlayerInv.AddItem(Item.WheatSeeds)
        
        
        
      

def MainMenu():
  print("\n [1] Farm \n [2] Inventory \n [3] Shop \n [4] Quit")           
  choice = input("What would you like to do? ")
  if choice == "1":
    pass
  elif choice == "2":
    pass
  elif choice == "3":
    ItmInst = items.Item
    Shop(ItmInst)
  elif choice == "4":
    print("Whatever, Hater.")
    sys.exit()

MainMenu()