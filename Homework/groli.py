lst = []
gro = {}

def count(ls):
    for i in range(len(ls)):
        if ls[i] in gro:
            gro[ls[i]] += 1
    return gro

while True:
    try:
        fru = input()
        lst.append(fru)
        gro[fru] = 0
    
    except (KeyboardInterrupt, EOFError):
        break

tro = count(lst)

for i in tro:
    print(f"{tro[i]} {i.upper()}")
