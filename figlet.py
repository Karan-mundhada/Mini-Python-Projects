import sys
import pyfiglet

while True:
    try:
        if(len(sys.argv) == 3 and sys.argv[1] == "-f"):
            a = input("Input: ")
            print("Output: ")
            pyfiglet.print_figlet(a, font=sys.argv[2])

        elif(len(sys.argv) == 1):
            a = input("Input: ")
            print("Output: ")
            pyfiglet.print_figlet(a)

        break
    except (ValueError, IndexError):
        print("Invalid Input or Not enough command line inputs")
        break