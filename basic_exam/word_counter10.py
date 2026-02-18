words = input().split(" ")

new_words = {}
current = 1

for word in words:
    if word in new_words:
        current+=1
        new_words.update({word : current})
    else:
        new_words.update({word : 1})

print(new_words)
