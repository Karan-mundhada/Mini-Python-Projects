temp = False
lst = []
camel = input("CamelCase: ")
for i in range(len(camel)):
    temp = camel[i].isupper()
    if temp == True:
        snake = camel.replace(camel[i], "_"+camel[i].lower())
        camel = snake
    temp = False

print(snake)