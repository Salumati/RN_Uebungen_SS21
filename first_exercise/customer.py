class Customer:
    def __init__(self, name, stationVisits, timeNextCustomer, shoppingList):
        self.name = name
        self.stationVisits = stationVisits
        self.timeNextCustomer = timeNextCustomer
        self.shoppingList = shoppingList
        # todo: Einkaufliste

    def productsForStation(self, station):
        return self.shoppingList[station]

    def startShopping(self):
        # create event to enter station
        self.stationVisits.next
        return

    def arriveStation(self):
        # crea
        return

    def leaveStation(self):

        return