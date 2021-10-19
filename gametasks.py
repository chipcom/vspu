from os import remove, rename

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName = ''):

    score = '-1'
    try:
        f = open('userScores.txt', 'r')

        for line in f:
            content = line.split(', ')
            if userName == content[0]:
                score = content[1]
    except IOError:
        f = open('userScores.txt', 'w')

    f.close()
    return score

def updateUserScore(newUser = False, userName = '', score = 0):

    if newUser:
        f = open('userScores.txt', 'a')
        f.write('\n' + userName + ', ' + str(score) )
        f.close()

print(getUserScore('Carol'))

updateUserScore(True, 'Vladimir', 50)