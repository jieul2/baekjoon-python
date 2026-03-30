def posToInt(data): 
    return 8 - int(data[1]), int(ord(data[0])) - 65

def intToPos(data):
    return str(chr(data[1]+65))+ str(8-data[0])

def isSamePos(king, rock):
    if king == rock:
        return True
    else:
        return False
def isOut(data):
    posData = posToInt(data)
    if 0 > posData[0] or 7 < posData[0] or 0 > posData[1] or 7 < posData[1]:
        return True
    else:
        return False
    

def move(move, king, rock):
    if(move == "R"):
        posIntKing = list(posToInt(king))
        posIntKing[1] += 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[1] -= 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[1] += 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[1] -= 1
                posIntRock[1] -= 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    
    elif(move == "L"):
        posIntKing = list(posToInt(king))
        posIntKing[1] -= 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[1] += 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[1] -= 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[1] += 1
                posIntRock[1] += 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    elif(move == "B"):
        posIntKing = list(posToInt(king))
        posIntKing[0] += 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[0] -= 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[0] += 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[0] -= 1
                posIntRock[0] -= 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    elif(move == "T"):
        posIntKing = list(posToInt(king))
        posIntKing[0] -= 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[0] += 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[0] -= 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[0] += 1
                posIntRock[0] += 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    elif(move == "RT"):
        posIntKing = list(posToInt(king))
        posIntKing[1] += 1
        posIntKing[0] -= 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[1] -= 1
            posIntKing[0] += 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[1] += 1
            posIntRock[0] -= 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[1] -= 1
                posIntRock[1] -= 1
                posIntKing[0] += 1
                posIntRock[0] += 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    elif(move == "LT"):
        posIntKing = list(posToInt(king))
        posIntKing[1] -= 1
        posIntKing[0] -= 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[1] += 1
            posIntKing[0] += 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[1] -= 1
            posIntRock[0] -= 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[1] += 1
                posIntRock[1] += 1
                posIntKing[0] += 1
                posIntRock[0] += 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    elif(move == "RB"):
        posIntKing = list(posToInt(king))
        posIntKing[1] += 1
        posIntKing[0] += 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[1] -= 1
            posIntKing[0] -= 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[1] += 1
            posIntRock[0] += 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[1] -= 1
                posIntRock[1] -= 1
                posIntKing[0] -= 1
                posIntRock[0] -= 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock
    elif(move == "LB"):
        posIntKing = list(posToInt(king))
        posIntKing[1] -= 1
        posIntKing[0] += 1
        king = intToPos(posIntKing)
         
        if isOut(king):
            posIntKing[1] += 1
            posIntKing[0] -= 1
            king = intToPos(posIntKing)
            return king, rock
        if isSamePos(king, rock):
            posIntRock = list(posToInt(rock))
            posIntRock[1] -= 1
            posIntRock[0] += 1
            rock = intToPos(posIntRock)
            if isOut(rock):
                posIntKing[1] += 1
                posIntRock[1] += 1
                posIntKing[0] -= 1
                posIntRock[0] -= 1
                king = intToPos(posIntKing)
                rock = intToPos(posIntRock)
                return king, rock
        return king, rock

    return king, rock


king, rock, count = input().split()

for _ in range(int(count)):
    king, rock = move(input(), king, rock)

print(king)
print(rock)
