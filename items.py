from main import Player
from main import PlayerInv

class Item:
  def __init__(self, name, price, description):
    self.name = name
    self.price = price
    self.description = description

WheatSeeds = Item("Wheat Seeds", 35, "Can be planted to grow wheat.")

Wheat = Item("Wheat", 50, "Can be sold at the shop.")

BlueberrySeeds = Item("Blueberry Seeds", 40, "Can be planted to grow blueberries.")

Blueberry = Item("Blueberries", 70, "Can be sold at the shop.")

HyacinthSeeds = Item("Hyacinth Seeds", 50, "Can be planted to grow Hyacinths.")

Hyacinth = Item("Hyacinth", 100, "Can be sold at the shop.")

RaspberrySeeds = Item("Raspberry Seeds", 60, "Can be planted to grow raspberries.")

Raspberry = Item("Raspberry", 110, "Can be sold at the shop.")

StrawberrySeeds = Item("Strawberry Seeds", 75, "Can be planted to grow strawberries.")

Strawberry = Item("Strawberry", 180, "Can be sold at the shop.")

WatermelonSeeds = Item("Watermelon Seeds", 100, "Can be planted to grow watermelons.")

Watermelon = Item("Watermelon", 175, "Can be sold at the shop.")

PearSapling = Item("Pear Sapling", 200, "Can be planted to grow a pear tree.")

Pear = Item("Pear", 300, "Can be sold at the shop.")

CherrySapling = Item("Cherry Sapling", 200, "Can be planted to grow a cherry tree.")

Cherry = Item("Cherry", 310, "Can be sold at the shop.")

LemonSapling = Item("Lemon Sapling", 200, "Can be planted to grow a lemon tree.")

Lemon = Item("Lemon", 300, "Can be sold at the shop.")


def Shop():
  print("Welcome! What can I do for ya'?")
  choice = input("\n [1] Buy \n [2] Sell \n [3] Leave")
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
    if choice == "1" and Player.currency >= WheatSeeds.price:
        Player.SubCurrency(WheatSeeds.price)
        PlayerInv.AddItem(WheatSeeds)

    elif choice == "2" and Player.currency >= BlueberrySeeds.price:
      Player.SubCurrency(BlueberrySeeds.price)
      PlayerInv.AddItem(BlueberrySeeds)

    elif choice == "3" and Player.currency >= HyacinthSeeds.price:
      Player.SubCurrency(HyacinthSeeds.price)
      PlayerInv.AddItem(HyacinthSeeds)

    elif choice == "4" and Player.currency >= RaspberrySeeds.price:
      Player.SubCurrency(RaspberrySeeds.price)
      PlayerInv.AddItem(RaspberrySeeds)

    elif choice == "5" and Player.currency >= StrawberrySeeds.price:
      Player.SubCurrency(StrawberrySeeds.price)
      PlayerInv.AddItem(StrawberrySeeds)

    elif choice == "6" and Player.currency >= WatermelonSeeds.price:
      Player.SubCurrency(WatermelonSeeds.price)
      PlayerInv.AddItem(WatermelonSeeds)

    elif choice == "7" and Player.currency >= PearSapling.price:
      Player.SubCurrency(PearSapling.price)
      PlayerInv.AddItem(PearSapling)

    elif choice == "8" and Player.currency >= CherrySapling.price:
      Player.SubCurrency(CherrySapling.price)
      PlayerInv.AddItem(CherrySapling)

    elif choice == "9" and Player.currency >= LemonSapling.price:
      Player.SubCurrency(LemonSapling.price)
      PlayerInv.AddItem(LemonSapling)

    else:
      print("I dont deal with poor folks...")
      pass


