
from player import PlayerInv
from player import Player
from items import Seeds


def Shop():
  print("Welcome! What can I do for ya'?")
  choice = input("\n [1] Buy \n [2] Sell \n [3] Leave")
  if choice == "1":
    print(f'[1] {Seeds.WheatSeeds}')
    print(f'[2] {Seeds.BlueberrySeeds}')
    print(f'[3] {Seeds.HyacinthSeeds}')
    print(f'[4] {Seeds.RaspberrySeeds}')
    print(f'[5] {Seeds.StrawberrySeeds}')
    print(f'[6] {Seeds.WatermelonSeeds}')
    print(f'[7] {Seeds.PearSapling}')
    print(f'[8] {Seeds.CherrySapling}')
    print(f'[9] {Seeds.LemonSapling}')
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
