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

Player = Farmer(500)

class Inventory:
  def __init__(self):
    self.inventory = []

  def AddItem(self,item):
    self.inventory.append(item)

  def RemoveItem(self, item):
    self.inventory.pop(item)

  def ShowInventory(self):
    print(self.inventory)


def Shop(Item):
  print("Welcome! What can I do for ya'?")
  choice = input("[1] Buy \n [2] Sell \n [3] Leave")
  if choice == "1":
    print(f'[1] {WheatSeeds}')
    print(f'[2] {BlueberrySeeds}')
    print(f'[3] {HyacinthSeeds}')
    print(f'[4] {RaspberrySeeds}')
    print(f'[5] {StrawberrySeeds}')
    print(f'[6] {WatermelonSeeds}')
    print(f'[7] {PearSapling}')
    print(f'[8] {CherrySapling}')
    print(f'[9] {LemonSapling}')
    print("[10] Leave")
    choice = input("What would you like to buy?")
    if choice == "1":
      amtchoice = input("How many would you like to buy?")
      if amtchoice * WheatSeeds.price <= Player.currency:
        Player.SubCurrency(amtchoice * WheatSeeds.price)
        Inventory.AddItem(amtchoice * WheatSeeds)
      else:
        print("You don't have enough money!")
      

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

