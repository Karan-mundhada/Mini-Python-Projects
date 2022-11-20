import emoji
x = input("Input: ")
ls = list(x.split())

for word in ls:
    for c in word:
        if c == ":":
            emo = emoji.emojize(word)
            e = x.replace(word, emo)

print(e)