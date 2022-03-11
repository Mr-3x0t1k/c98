def countWords():
    fileName = input("enter the file name: ")
    no_of_words = 0
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        no_of_words = no_of_words+len(words)
    print("number of words = ")
    print(no_of_words)
    
countWords()
