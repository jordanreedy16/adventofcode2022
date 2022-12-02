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

def actionPickers(opChoice, outcome):
    # chooses a response based on the opponent choice and desired outcome
    # Choice if rock is selected
    if opChoice == 'A':
        if outcome == 'X':
            playerResponse = 'Z'
        elif outcome == 'Y':
            playerResponse = 'X'
        elif outcome == 'Z':
            playerResponse = 'Y'
    
    if opChoice == 'B':
        if outcome == 'X':
            playerResponse = 'X'
        elif outcome == 'Y':
            # draw. Paper and paper
            playerResponse = 'Y'
        elif outcome == 'Z':
            # win. Paper beaten by scissors
            playerResponse = 'Z'

    if opChoice == 'C':
        if outcome == 'X':
            #loss
            playerResponse = 'Y'
        elif outcome == 'Y':
            #draw
            playerResponse = 'Z'
        elif outcome == 'Z':
            #win
            playerResponse = 'X'

    return playerResponse

with open('input.txt') as cheatSheet:
    totalPoints = 0
    for line in cheatSheet:
        line = line.split()
        opponentChoice = line[0]
        outcomeNeeded = line[1]

        playerChoice = actionPickers(opponentChoice, outcomeNeeded)

        totalPoints = (checkMatch(opponentChoice, playerChoice) + calcDecisionModifiers(playerChoice) + totalPoints)
        
    print(f"Game Points: {totalPoints}")