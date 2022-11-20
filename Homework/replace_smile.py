def main():
    x = input()
    convert(x)

def convert(str1):
    if ":)" in str1:
        print(str1.replace(":)", "🙂"))
    elif ":(" in str1:
        print(str1.replace(":(", "🙁"))

main()