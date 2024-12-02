sentence = input("Enter a Sentence: ") + " "
number_of_words = 0
for i in sentence : 
    if i == " "  :
        number_of_words += 1
    elif i == "?" or i == "!" or i == "." :
        number_of_words += 1
        break
print("Number of Words in the Sentence = ",number_of_words)