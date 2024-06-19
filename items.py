
class Item:
  def __init__(self, name, price, description):
    pass


class Seeds(Item):
  WheatSeeds = Item("Wheat Seeds", 35, "Can be planted to grow wheat.")
  BlueberrySeeds = Item("Blueberry Seeds", 40, "Can be planted to grow blueberries.")
  HyacinthSeeds = Item("Hyacinth Seeds", 50, "Can be planted to grow Hyacinths.")
  RaspberrySeeds = Item("Raspberry Seeds", 60, "Can be planted to grow raspberries.")
  StrawberrySeeds = Item("Strawberry Seeds", 75, "Can be planted to grow strawberries.")
  WatermelonSeeds = Item("Watermelon Seeds", 100, "Can be planted to grow watermelons.")
  PearSapling = Item("Pear Sapling", 200, "Can be planted to grow a pear tree.")
  CherrySapling = Item("Cherry Sapling", 200, "Can be planted to grow a cherry tree.")
  LemonSapling = Item("Lemon Sapling", 200, "Can be planted to grow a lemon tree.")
pass


class Crops(Item):
  Wheat = Item("Wheat", 50, "Can be sold at the shop.")
  Blueberry = Item("Blueberries", 70, "Can be sold at the shop.")
  Hyacinth = Item("Hyacinth", 100, "Can be sold at the shop.")
  Raspberry = Item("Raspberry", 110, "Can be sold at the shop.")
  Strawberry = Item("Strawberry", 180, "Can be sold at the shop.")
  Watermelon = Item("Watermelon", 175, "Can be sold at the shop.")
  Pear = Item("Pear", 300, "Can be sold at the shop.")
  Cherry = Item("Cherry", 310, "Can be sold at the shop.")
  Lemon = Item("Lemon", 300, "Can be sold at the shop.")
pass

