# def adi(l1):
#     l = len(l1)
#     print("Adieu, adieu, to", end=" ")
#     for i in range(l):
#         if(i == l-1):
#             print(f"and {l1[-1]}.")
#         else:
#             print(f"{l1[i]},", end=" ")
import inflect
p = inflect.engine()

lis = []

while True: 
    try:
        n = input("Name: ")
        lis.append(n)

    except KeyboardInterrupt:
        print()
        print("Adieu, adieu, to",p.join(lis))
        break