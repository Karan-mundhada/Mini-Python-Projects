import collections

t = int(input())
lst = []

def max_count(lst1):
    c = len(lst1)
    dict1 = dict(collections.Counter(lst1))
    
    lst2 = []
    for j in range(c):
        lst2.append(dict1[lst1[j]])
    m = max(lst2)
    return m

for i in range(t):
    n = int(input())
    lst1 = list(map(int, input().split()))
        
    
    m1 = max_count(lst1)
    if(m1 == 2):
        m2 = m1
    elif(m1%2 == 0):
        m2 = m1/2
    else:
        m2 = m1//2 + 1
    
    lst.append(m2)

for u in range(t):
    print(lst[u])
