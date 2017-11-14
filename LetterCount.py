def LetterCount(str):

    lista=list(str)
    #print (lista)
    lDicc= {}
    for i in lista:
        if i in lDicc:
            lDicc[i] +=1
        else:
            lDicc[i]= 1
    print (lDicc)

word = input("Enter a Word: ")

LetterCount(word)