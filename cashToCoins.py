dollarAmount = 8.69
piggyBank = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}
coinValues = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01
}
def convert_to_coins(amount, bank, coinValues):
    for key in bank:
        while amount + 0.01 > coinValues[key]:
            bank[key] += 1
            amount -= coinValues[key]
convert_to_coins(dollarAmount, piggyBank, coinValues)
print(piggyBank)