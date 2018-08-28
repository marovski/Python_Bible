sentence=input("Write a sentece: ").lower().split()
finalSentence=[]
for words in sentence:
    if words[0] in "aeiou":
        words = words + "yay"
       
    else:
        words=words[1:]+words[0]+"ay"

    finalSentence.append(words)

print(" ".join(finalSentence))






