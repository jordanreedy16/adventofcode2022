def checkMatch(opChoice, yourChoice):
    # Check if match contains win criteria. If so, set outcomePoints to 6, indicating a win.
    if (opChoice == 'C' and yourChoice == 'X') or (opChoice == 'A' and yourChoice == 'Y') or (opChoice == 'B' and yourChoice == 'Z'):
        outcomePoints = 6
    elif (opChoice == 'A' and yourChoice == 'X') or (opChoice == 'B' and yourChoice == 'Y') or (opChoice == 'C' and yourChoice == 'Z'):
        outcomePoints = 3 #draw
    elif (opChoice == 'B' and yourChoice == 'X') or (opChoice == 'C' and yourChoice == 'Y') or (opChoice == 'A' and yourChoice == 'Z'):
        outcomePoints = 0 # loss

    return outcomePoints

def calcDecisionModifiers(yourChoice):
    # Check which action was taking and return integer representing points modifier for choice
    if yourChoice == 'X':
        pointsModifier = 1
    elif yourChoice == 'Y':
        pointsModifier = 2
    elif yourChoice == 'Z':
        pointsModifier = 3

    return pointsModifier

with open('input.txt') as cheatSheet:
    totalPoints = 0
    for line in cheatSheet:
        line = line.split()
        opponentChoice = line[0]
        playerChoice = line[1]

        totalPoints = (checkMatch(opponentChoice, playerChoice) + calcDecisionModifiers(playerChoice) + totalPoints)
        
    print(f"Game Points: {totalPoints}")