def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    j = 1
    if (2 <= len(s) <= 6) and s.isalnum() and s[:2].isalpha():
        for c in s:
            if c.isdigit():
                k = s.index(c)
                if(s[k:].isdigit() and s[k] != '0'):
                    print(s[k],k,int(c))
                    return True
                else:
                    return False
        

main()