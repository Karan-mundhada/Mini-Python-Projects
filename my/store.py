class store:
    def __init__(self,name,price,code):
        self.name = name
        self.code = code
        self.price = price
t = [store("adranaline", 500, 'abr'),store("oxytocin", 400, 'oxy'),
    store("morphine", 600, 'mor'),store("aspirine", 200, 'asp'),
    store("injection", 20,'inj'),store("cotton", 50, 'cot')]

# for i in range(len(t)):    
#     print("name -", t[i].name ,"price -",t[i].price, "code -", t[i].code)

x = list(map(str, input("Input code of the Items you would like to buy: ").split()))
total = 0

for i in range(len(x)):
    for j in range(len(t)):
        if x[i] == t[j].code:
            print(t[j].name, '-' ,t[j].price)
            print(f"how many {t[j].name} do you need: ", end="")
            n = int(input())
            total = total + t[j].price*n
    print()

print("total bil =", total)