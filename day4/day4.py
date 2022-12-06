def checkArrays(area1Range, area2Range):
    match = 0

    if set(area1Range).issubset(area2Range):
        match = 1
    elif set(area2Range).issubset(area1Range):
        match = 1
    else:
        match = 0

    return match

def checkAnyOverlap(area1Range, area2Range):
    match = 0 
    for num in area1Range:
        for num2 in area2Range:
            if num == num2:
                match = 1
                return match

    return match

def fillRange(area1, area2):
    area1Split = area1.split('-')
    area2Split = area2.split('-')

    area1Min = int(area1Split[0])
    area1Max = int(area1Split[1])

    area2Min = int(area2Split[0])
    area2Max = int(area2Split[1])

    area1Range = list(range(area1Min, area1Max+1))

    area2Range = list(range(area2Min, area2Max+1))

    area1String = ''
    area2String = ''

    # if area1Min == area1Max:
    #     area1String = str(area1Min)
    # elif area1Min != area1Max:
    #     for number in area1Range:
    #         area1String += str(number)

    # if area2Min == area2Max:
    #     area2String = str(area2Min)
    # elif area2Min != area2Max:
    #     for number in area2Range:
    #         area2String += str(number)

    match = checkArrays(area1Range, area2Range)

    if match == 0:
        match = checkAnyOverlap(area1Range, area2Range)

    return match


    


total = 0

with open('input.txt') as cleaningAreas:
    for line in cleaningAreas:
        areaTuple = (line.strip()).split(',')
        area1 = areaTuple[0]
        area2 = areaTuple[1]
        matchValue = fillRange(area1, area2)
        total += matchValue

        
    print(f'Total Matches: {total}')
    