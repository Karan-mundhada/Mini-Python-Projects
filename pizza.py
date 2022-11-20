import sys
from tabulate import tabulate

try:
    if(len(sys.argv) == 2):
        with open(f"{sys.argv[1]}", 'r') as ff:
            lines = []
            for line in ff:    
                lines.append(list(line.rstrip().split(",")))
            
            print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    elif(len(sys.argv) < 2):
        print("Too few arguments")
        sys.exit()
    
    elif(len(sys.argv) > 2):
        print("Too many arguments")
        sys.exit()


except FileNotFoundError:
    print("File not found")
    sys.exit()