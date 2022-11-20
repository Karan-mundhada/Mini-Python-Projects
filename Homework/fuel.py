def frac():
    while True:
        n = input("Fraction: ")
        k = n.index("/")
        try:    
            x = int(n[:k])
            y = int(n[k+1:])
            c = x/y
            return c

        except (ValueError, ZeroDivisionError):
            continue

def main():
    c = frac()
    if(c == 0):
        print("E")
    elif(c == 1):
        print("F")
    elif(c > 1):
        c = frac()
    else:
        g = c*100
        print(f"Fraction: {int(g)}%")

main()