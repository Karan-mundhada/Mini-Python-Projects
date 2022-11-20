def main():
    word = input("Input: ")
    print("output:", shorten(word))

def shorten(w):
    vowel = ['a', 'e', 'i', 'o', 'u', "A", 'U']
    ls = list(w)
    lis = []
    
    for c in ls:
        if c in vowel:
            lis.append(c)
    
    for c in lis: 
        ls.remove(c)

    wo = "".join(ls)
    return wo

if __name__ == "__main__":
    main()