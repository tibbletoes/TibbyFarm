
from inventory import PlayerBal
from inventory import PlayerInv

class Item:
  def __init__(self, name, price, description):
    self.name = name
    self.price = price
    self.description = description

WheatSeeds = Item("Wheat Seeds", 35, "Can be planted to grow wheat.")
BlueberrySeeds = Item("Blueberry Seeds", 40, "Can be planted to grow blueberries.")
HyacinthSeeds = Item("Hyacinth Seeds", 50, "Can be planted to grow Hyacinths.")
RaspberrySeeds = Item("Raspberry Seeds", 60, "Can be planted to grow raspberries.")
StrawberrySeeds = Item("Strawberry Seeds", 75, "Can be planted to grow strawberries.")
WatermelonSeeds = Item("Watermelon Seeds", 100, "Can be planted to grow watermelons.")
PearSapling = Item("Pear Sapling", 200, "Can be planted to grow a pear tree.")
CherrySapling = Item("Cherry Sapling", 200, "Can be planted to grow a cherry tree.")
LemonSapling = Item("Lemon Sapling", 200, "Can be planted to grow a lemon tree.")

Wheat = Item("Wheat", 50, "Can be sold at the shop.")
Blueberry = Item("Blueberries", 70, "Can be sold at the shop.")
Hyacinth = Item("Hyacinth", 100, "Can be sold at the shop.")
Raspberry = Item("Raspberry", 110, "Can be sold at the shop.")
Strawberry = Item("Strawberry", 180, "Can be sold at the shop.")
Watermelon = Item("Watermelon", 175, "Can be sold at the shop.")
Pear = Item("Pear", 300, "Can be sold at the shop.")
Cherry = Item("Cherry", 310, "Can be sold at the shop.")
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
    if choice == "1" and PlayerBal.currency >= WheatSeeds.price:
        PlayerBal.SubCurrency(WheatSeeds.price)
        PlayerInv.AddItem(WheatSeeds)

    elif choice == "2" and PlayerBal.currency >= BlueberrySeeds.price:
      PlayerBal.SubCurrency(BlueberrySeeds.price)
      PlayerInv.AddItem(BlueberrySeeds)

    elif choice == "3" and PlayerBal.currency >= HyacinthSeeds.price:
      PlayerBal.SubCurrency(HyacinthSeeds.price)
      PlayerInv.AddItem(HyacinthSeeds)

    elif choice == "4" and PlayerBal.currency >= RaspberrySeeds.price:
      PlayerBal.SubCurrency(RaspberrySeeds.price)
      PlayerInv.AddItem(RaspberrySeeds)

    elif choice == "5" and PlayerBal.currency >= StrawberrySeeds.price:
      PlayerBal.SubCurrency(StrawberrySeeds.price)
      PlayerInv.AddItem(StrawberrySeeds)

    elif choice == "6" and PlayerBal.currency >= WatermelonSeeds.price:
      PlayerBal.SubCurrency(WatermelonSeeds.price)
      PlayerInv.AddItem(WatermelonSeeds)

    elif choice == "7" and PlayerBal.currency >= PearSapling.price:
      PlayerBal.SubCurrency(PearSapling.price)
      PlayerInv.AddItem(PearSapling)

    elif choice == "8" and PlayerBal.currency >= CherrySapling.price:
      PlayerBal.SubCurrency(CherrySapling.price)
      PlayerInv.AddItem(CherrySapling)

    elif choice == "9" and PlayerBal.currency >= LemonSapling.price:
      PlayerBal.SubCurrency(LemonSapling.price)
      PlayerInv.AddItem(LemonSapling)

    else:
      print("I dont deal with poor folks...")
      pass
