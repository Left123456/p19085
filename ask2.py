print ("Είσοδος κειμένου μέσω του αρχείου 2.txt")
textfile = open("2.txt","r")
words = txtfile.read()
words =words.split()
badLetters =["f","c","k","r"]
notConsonants = ["a","e","i","o","u","y",",","."]

for word in words:
    badCounter = 0
    normalCounter = 0
    for letter in words:
        if letter in word:
            badCounter += 1
        elif letter not in notConsonants:
            normalCounter += 1
    
    if (badCounter > normalCounter) and (len(word) > 3):
        print("Found potential bad word:" + word)