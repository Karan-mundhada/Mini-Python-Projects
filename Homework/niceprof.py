import random


def get_level():
    while True:    
        try:
            lvl = int(input("Level: "))
            if(lvl == 1 or lvl == 2 or lvl == 3):
                k = go_prob(lvl)
                print(f"Score: {10 - k}")
                break
            else:
                raise ValueError

        except ValueError:
            continue


def go_prob(l):  
    test = 10 
    wcount = 0
    while(test > 0):
        n = (10)**(l-1)
        f = random.randint(n, (10*n) - 1)
        g = random.randint(n, (10*n) - 1)
        ans = int(input(f"{f} + {g} = "))
        if(ans == f+g):
            test -= 1
        else:
            wcount += 1
            test = test - wrong_ans(f,g)
            continue

    #older bogas design
    # if(l == 1):
    #     while(test > 0):
    #         f = random.randint(1, 9)
    #         g = random.randint(1, 9)
    #         ans = int(input(f"{f} + {g} = "))
    #         if(ans == f+g):
    #             test -= 1
    #         else:
    #             wcount += 1
    #             test = test - wrong_ans(f,g)
    #             continue
    # elif(l == 2):
    #     while(test > 0):
    #         f = random.randint(10, 99)
    #         g = random.randint(10, 99)
    #         ans = int(input(f"{f} + {g} = "))
    #         if(ans == f+g):
    #             test -= 1
    #         else:
    #             wcount += 1
    #             test = test - wrong_ans(f,g)
    #             continue
    # elif(l == 3):
    #     while(test > 0):
    #         f = random.randint(100, 999)
    #         g = random.randint(100, 999)
    #         ans = int(input(f"{f} + {g} = "))
    #         if(ans == f+g):
    #             test -= 1
    #         else:
    #             wcount += 1
    #             test = test - wrong_ans(f,g)
    #             continue
    return wcount


def wrong_ans(s1, s2):
    count = 1
    print("EEE")
    while(count < 3):
        ans = int(input(f"{s1} + {s2} = "))
        if(ans == s1+s2):
           return 1
        else:
            print("EEE")
            count += 1
    print(f"{s1} + {s2} = {s1+s2}")
    return 1


def main():
    get_level()


main()
