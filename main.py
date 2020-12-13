
def displayResults (resultsTable):
  results = []
  for key in resultsTable:
    i = 0
    while i < resultsTable[key]:
      results.append(key)
      i += 1
  return results

numberOfDice = 4 # number of dice
def generateResultsTable(dice):
  pattern = [1,1,1,1,1,1]

  while len(pattern) <= 5*numberOfDice:
    dice = 1+len(pattern)//5
    possibleResults = list(range(dice, 6*dice+1))

    difference = []
    aSet = pattern[1:] + [0,0,0,0,0]
    bSet = list(reversed(aSet))
    size = len(aSet)
    for i in range(size):
      difference.append(aSet[i]-bSet[i])

    #print(difference)

    number = 1
    results = []
    results.append(number)
    for i in difference:
      number += i
      results.append(number)

    table = {}
    if len(possibleResults) == len(results):
      for i in range(len(results)):
        table[possibleResults[i]] = results[i]
    

    #print(f"Dice: {dice} Results:", table)
    #print(results)
    pattern = results
  return table

stuff = generateResultsTable(numberOfDice)
print(stuff)