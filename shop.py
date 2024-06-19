
from inventory import PlayerBal
from inventory import PlayerInv
from items import WheatSeeds, BlueberrySeeds, HyacinthSeeds, RaspberrySeeds, StrawberrySeeds, WatermelonSeeds, PearSapling, CherrySapling, LemonSapling



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
