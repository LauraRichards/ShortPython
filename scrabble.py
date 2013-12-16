#!/usr/bin/python
#Laura Richards 2013

'''
Takes in a string and prints out a list of the longest words that can be created with the letters
'''

import sys

'''
Takes in a string
Returns a dict where key->value is letter->#times in string
'''
def countTiles(inputString):

    tiles = dict()    
    for letter in inputString:
        if(letter in tiles):
            tiles[letter] += 1
        else:
            tiles[letter] = 1
            
    return tiles
    
    
''' Change the sort function to compare by length '''
def sortWords(x):
    def sortLength(word1, word2):
        return len(word2) - len(word1)
        
    x.sort(cmp=sortLength)
    return x
    

''' 
	Takes in the # of tiles, a dict() of the tiles and a list of the dictoniary words   
	Returns a list of the longest words that can be created with the given tiles
'''
def findLongest(stringLength, tiles, wordsDict):

    longestWords = []
    
    for word in wordsDict:
        if(len(word) <= stringLength):  #only check the words with a maximum length of the #of tiles
        
            goodFlag = 1
            lettersInDictWord = dict()
                        
            for letter in word:  # make a dict() for every letter in the current word                     
                if(letter in lettersInDictWord):
                    lettersInDictWord[letter] += 1
                else:
                    lettersInDictWord[letter] = 1
                             
            # check to see if there are enough tiles to make the word. First word found will be the longest one that can be made.
            for letterKey in lettersInDictWord:           
                if( letterKey not in tiles or lettersInDictWord[letterKey] > tiles[letterKey]): 
                    goodFlag = -1
                    break
             
            # make a list of the longests word(s) you can create
            if(goodFlag == 1):               
                if(len(longestWords) > 0 and len(word) < len(longestWords[0])): # current word that can be created is shorter therefore stop looking
                    break              
                longestWords.append( word ) 
                
    return longestWords           
    

def main():

    if(len(sys.argv) == 1):
       print "You need to supply a string"
       sys.exit(1)
    
    
    inputString = (sys.argv[1]).lower()
    
    if(not inputString.isalpha()):
        print "You need to supply a string without numbers"
        sys.exit(1)
        
    print "You have inputted: "+ inputString
    
    IF = open("/usr/share/dict/words", 'r') # doc with words

    # Make a list of dictonary words
    wordsDict = []
    for word in IF:       
        wordsDict.append( word.strip() )
        
    tiles = countTiles(inputString)
    wordsDict = sortWords(wordsDict) # sorts words by decresing length
    goodWords = findLongest(len(inputString), tiles, wordsDict)

    
    print "Here are the longest word(s) that can be created:"
    print goodWords
    
    
if __name__ == '__main__':
    main()