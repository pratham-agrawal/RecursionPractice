M = int(input())
N = int(input())

table = []
for i in range (M):
    line = input().split()
    table.append(line)

m=0
while m < M:
    n=0
    while n < N:
        table[m][n] = int(table[m][n])
        n+=1
    m+=1

def findFactors(number):
    factorList = []
    for i in range (1, number+1):      #ceiling
        if number % i == 0 and i <= M and (number/i)<=N:
            factorList.append([i, int(number/i)])
    return(factorList)

pastLocations = []
def recursive(number):
    factorList = findFactors(number)
    for i in factorList:
        if i[0] == M and i[1] == N:
            return True
        else:
            newList = [i[0], i[1]]
            if newList not in pastLocations:
                pastLocations.append(newList)
                newNum = table[i[0]-1][i[1]-1]
                if recursive(newNum) == True:
                    return True
            else:
                return False
    return False

if recursive(table[0][0]) == True:
    print("yes")
else:
    print("no")