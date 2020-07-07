import sys
def isLetter(character):
    diff1 = int(ord(character)) - int(ord('A'))
    diff2 = int(ord(character)) - int(ord('a'))

    if diff1 >= 0 and diff1 <= 25:
        return True
    if diff2 >= 0 and diff2 <= 25:
        return True
    return False
def saveToFile(wordList, wordCount, wordOccurrences):
    '''Writes the order of words and number of each word to output.txt'''
    output = open("../output.txt", "w")
    output.write(str(len(wordCount.keys())) + "\n")
    for word in wordCount.keys():
        output.write(word + ": " + str(wordCount.get(word)) + "\n")
    counter = 0
    for word in wordList:
        output.write(word)
        counter += 1

        if counter == 20:
            output.write("\n")
            counter = 0
        else:
            output.write(" ")
    output.close()

def loadFromFile(filename):
    '''Loads list of words and occurrences of each word from file'''
    wordList = []
    wordOccurrences = dict()

    '''First, gets number of distinct words in text and reads dictionary recording number of occurrences'''
    input = open("../output.txt", "r")
    numWords = int(input.readline())
    for i in range(numWords):
        lineWords = input.readline().split(":")
        keyword = lineWords[0]
        numOccurrences = int(lineWords[1])
        wordOccurrences[keyword] = numOccurrences
    
    '''Then, reads the remaining lines, which represent the syllabus text'''
    syllabiLines = input.readlines()

    for line in syllabiLines:
        wordList.extend(line.split())

    return wordList, wordOccurrences



def clean(word):
    '''Removes non-letters/numbers from each word.'''
    newWord = ""

    for character in word:
        if isLetter(character):
            newWord += character
    return newWord.lower()   

def query(filename, keywordList):     
    '''Returns the query information for the keywords'''
    '''If the text contains the keyword, the value will be a positive number, otherwise it's N/A'''
    wordList, wordOccurrences = loadFromFile(filename)
    
    '''
    for word in wordList:
        print(word)

    for key in wordOccurrences.keys():
        print(key + " : " + str(wordOccurrences[key]))
    '''


    keywordOccurrences = dict()

    for keyword in keywordList:
        '''print(keyword)'''
        keywordOccurrences[keyword] = "N/A"
        if keyword in wordOccurrences:
            keywordOccurrences[keyword] = wordOccurrences[keyword]
        '''print(str(keywordOccurrences[keyword]))'''
        



    return keywordOccurrences

def parse(filename): 
    '''Parses the syllabi into bag-of-words and records it in a file'''

    input = open("../output/syllabi_text/" + filename)
    print("ok")

    wordCount = dict()
    wordOccurrences = dict()
    wordList = []



    lines = input.readlines()
    wordCounter = 0

    for line in lines: 
        '''Parses file into lines, lines are split into words based on whitespace'''
        '''Count of each word and order of words is updated'''
        words = line.split()
        for word in words:
            cleanedWord = clean(word)
            if cleanedWord not in wordCount:
                wordCount[cleanedWord] = 1
                wordOccurrences[cleanedWord] = [wordCounter]
            else:
                wordCount[cleanedWord] = wordCount[cleanedWord] + 1
                wordOccurrences[cleanedWord].append(wordCounter)
            wordCounter += 1
            wordList.append(cleanedWord)

    '''
    For debugging purposes to see what words are there/how much they occurr
    for word in wordList:
        print("Word: " + word)

    for word in wordCount.keys():
        print("Word: " + word + " Count: " + str(wordCount[word]))
    '''

    saveToFile(wordList, wordCount, wordOccurrences)


def main():
    '''The arguments look like this after python nlp.py'''
    '''[command] [filename] [list of keyword arguments]'''
    '''Command tells the program whether to turn syllabi into bag of words('parse') or answer keyword queries on a syllabus('query')'''
    '''Filename(syllabus_n.txt) is only for parsing certain syllabi documents, and just insert a dummy argument here for keyword queries'''
    '''Keyword arguments represent the searched keywords for the syllabi'''
    '''First run the program in parse mode on a syllabus, and then call query mode'''

    '''Allows for custom syllabus file argument'''
    filename = sys.argv[2]

    '''Determines what to do'''
    command = sys.argv[1].lower()
    if command != "query" and command != "parse":
        print("Command not recognized")
        return

    keywordList = []
    for i in range(3, len(sys.argv)):
        keywordList.append(sys.argv[i].lower())
    

    if command == "query" and len(keywordList) == 0:
        print("Query option specified but no keywords passed in")
        return

    if command == "parse":
        parse(filename)

    else:
        return query(filename, keywordList)

if __name__ == '__main__':
    main()
