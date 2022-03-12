while True:
    Length = input("Enter Your length Value : ")
    if Length.isnumeric():
        Length = int(Length)
        break


while True:
    startVal = input("Enter Your Start Value : ")
    if startVal.isnumeric():
        startVal = int(startVal)
        break


def specificLength(usrLength=0, start=0):
    counter = 0
    creatingList = []
    for num in range(usrLength):
        creatingList.append(start)
        start += 1
        counter += 1
    return [creatingList, counter]


mylist = specificLength(Length, startVal)
print(mylist)
