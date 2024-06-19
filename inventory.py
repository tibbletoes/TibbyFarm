

class Farmer:
  def __init__(self, currency):
    self.currency = currency

  def AddCurrency(self, amount):
    self.currency += amount

  def SubCurrency(self,amount):
    self.currency -= amount

  def ShowCurrency(self):
    print(f'Balance: {self.currency}')
pass


class Inventory:
  def __init__(self):
    self.inventory = []

  def AddItem(self,item):
    self.inventory.append(item)

  def RemoveItem(self, item):
    self.inventory.pop(item)

  def ShowInventory(self):
    print(self.inventory)
pass


PlayerBal = Farmer(500)
PlayerInv = Inventory()