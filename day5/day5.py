import re

def getArray(arrayNum):
    array = ''
    if arrayNum == 1:
        array = array1
    elif arrayNum == 2:
        array = array2
    elif arrayNum == 3:
        array = array3
    elif arrayNum == 4:
        array = array4
    elif arrayNum == 5:
        array = array5
    elif arrayNum == 6:
        array = array6
    elif arrayNum == 7:
        array = array7
    elif arrayNum == 8:
        array = array8
    elif arrayNum == 9:
        array = array9

    return array

def printArrays():
    print(array1)
    print(array2)
    print(array3)
    print(array4)
    print(array5)
    print(array6)
    print(array7)
    print(array8)
    print(array9)

def maintainOrder(sourceArray, destArray, moveValue):
    arrayLength = len(sourceArray)
    arrayLength += 1
    bottom = arrayLength - moveValue
    print(arrayLength)
    print(destArray)
    for i in range(arrayLength, bottom, -1):
        print(sourceArray[i])
    



array1 = ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T']
array2 = ['Q', 'R', 'B']
array3 = ['B', 'Z', 'T', 'Q', 'P', 'M', 'S']
array4 = ['D', 'V', 'F', 'R', 'Q', 'H']
array5 = ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P']
array6 = ['W', 'R', 'T', 'Z']
array7 = ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J']
array8 = ['R', 'N', 'F', 'H', 'W']
array9 = ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']

with open('input.txt') as crateMoves:
    for line in crateMoves:
        digits = re.findall(r'\d+', line.strip())
        moveValue = int(digits[0])
        source = int(digits[1])
        destination = int(digits[2])

        sourceStack = getArray(source)
        destStack = getArray(destination)

        for number in range(0, moveValue):
            crate = sourceStack.pop()
            destStack.append(crate)
            print(f'Source Stack: {sourceStack}')
            print(f'Dest Stack: {destStack}')

printArrays()
maintainOrder(sourceStack, destStack, moveValue)