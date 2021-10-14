
users = {
    "Aidan": 10000,
    "Alex": 20,
    "Conor": 69420
}

class GasBill():
    def __init__(self, standingCharge = 50, price = 5):
        self.standingCharge = standingCharge
        self.price = price

    def getReading(self):
        reading = int(input("Current reading: "))
        return reading

    def calculateUnits(self,reading):
        oldReading = int(input("Old reading: "))
        return reading - oldReading

    def calculateBalance(self, totalUnits, balance):
        return balance - ((totalUnits * self.price) + self.standingCharge)

    def generateBill(self, balance, units):
        print(f"\nYour bill:\nWe subtracted £{float(units)} and a £{float(self.standingCharge)} standing charge from your account\n\nYour current balance: £{float(balance)}")

#Insert params when class called - if params not inserted then the default values are used
gasBill = GasBill(20, 1)
reading = gasBill.getReading()
units = gasBill.calculateUnits(reading)
balance = gasBill.calculateBalance(units, users["Aidan"])

gasBill.generateBill(balance, units)

input("Press ENTER to return")