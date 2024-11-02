import os


def isSpanish(str):
    data = str.split(",")
    for i in range(1,6):
        if(not (i == 1 and data[i] == 1)):
            return False
        elif(i != 1 and data[i] == 1):
            return False
    return True
def isEnglish(srt):
    data = str.split(",")
    for i in range(1,6):
        if(data[i] == 1):
            return False

def returnAllFiles(path, word, languages, trans, num):
    dir_list = os.listdir(path)
    filesToReturn = []

    for file in dir_list:
        goodFile = False
        goodFile1 = False
        goodFile2 = False
        goodFile3 = False

        newFilename = file[:-4]
        dataArray = newFilename.split("_")
        if(len(dataArray) != 4):
            #print(dataArray)
            continue
        if(len(word) == 0  or word.count(dataArray[0]) > 0 ):
            goodFile = True
        if(len(languages) == 0 or languages.count(dataArray[1]) > 0):
            goodFile1 = True
        if(len(trans) == 0 or trans.count(dataArray[2]) > 0):
            goodFile2 = True
        if(len(num) == 0 or num.count(dataArray[3]) > 0):
            goodFile3 = True

        if goodFile and goodFile1 and goodFile2 and goodFile3:
            filesToReturn.append(file)
    return filesToReturn

def languagesSpoken(path, span,fren,german,other):
    listOfPeople = []
    MetaDataFile = open(path + "metadata.csv", "r")
    for line in MetaDataFile:
        if line[0] == "p":
            continue
        else:
            filteredLine = line[:-1]
            data = filteredLine.split(",")
            goodPerson = True
            if (len(span) != 0 and span.count(data[1]) == 0):
                goodPerson = False
            if (len(fren) != 0 and fren.count(data[2]) == 0):
                goodPerson = False
            if (len(german) != 0 and german.count(data[3]) == 0):
                goodPerson = False
            if (len(other) != 0 and other.count(data[4]) == 0):
                goodPerson = False

            if(goodPerson):
                listOfPeople.append(data[0])

    return listOfPeople



# Get the list of all files and directories
path = "C://Users//alber//Documents//School//Clubs//Data Challenge//EEG_Measurements"
path2 =  "C://Users//alber//Documents//School//Clubs//Data Challenge//"


#filesToTest = returnAllFiles(path, ["shoe"], ["english-spanish"], [], ["1","2","3","4"])

peopleToTest = languagesSpoken(path2, ["0"],["0"],["0"],["0"])


# prints all files
for file in peopleToTest:
    print(file + "\n")