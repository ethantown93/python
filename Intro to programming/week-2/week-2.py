companyName = 'Apple'
fiberLength = 20

def calculate(fiber, companyName):
    totalCost = fiber * .87
    print('Hello ' + companyName + ', ' + 'the total cost of your fiber order is ' + str(totalCost))

calculate(fiberLength, companyName)