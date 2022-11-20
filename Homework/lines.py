import sys

try:
    if(len(sys.argv) == 2):
        with open(f"{sys.argv[1]}", 'r') as ff:
            lines = ff.readlines()

        count = 0
        for line in lines:
            if(len(line.strip()) > 0):    
                count = count + 1

        print(count)

    elif(len(sys.argv) < 2):
        print("Too few arguments")
        sys.exit()
    
    elif(len(sys.argv) > 2):
        print("Too many arguments")
        sys.exit()


except FileNotFoundError:
    print("File not found")
    sys.exit()
