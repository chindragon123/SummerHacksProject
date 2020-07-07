from transformers import pipeline
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
    output = open("output.txt", "w")
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

def clean(word):
    '''Removes non-letters/numbers from each word.'''
    newWord = ""

    for character in word:
        if isLetter(character):
            newWord += character
    return newWord.lower()        

def main1(): 
    '''Current code for question-answering. Can run this with several questions asking for class features and use scores to evaluate the answers'''
    print("Leggo")
    nlp = pipeline('question-answering')
    print(nlp({
        'question': 'Does this class teach about the Renaissance',
        'context': 'The course covers everything from Renaissance history including Leonardo da Vinci and Michaelangelo. It however, does not go deep into detail of the post-Renaissance era. Other graduate courses are responsible for covering that.'}
    ))

def main():
    filename = "syllabus_0.txt"
    
    '''Allows for custom syllabus file argument'''
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    input = open("output/test_text/" + filename)

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

    
    for word in wordList:
        print("Word: " + word)

    for word in wordCount.keys():
        print("Word: " + word + " Count: " + str(wordCount[word]))

    saveToFile(wordList, wordCount, wordOccurrences)

if __name__ == '__main__':
    main1()
