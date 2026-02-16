sentence = "python is great and python is powerful"

words = sentence.split(" ")


map = {}

for raw_word in words :
    word = raw_word.lower()
    if word in map :
        map[word] +=1
    else :
        map[word] = 1
print(map)
