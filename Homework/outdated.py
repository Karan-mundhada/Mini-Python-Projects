ml = {"January": '01',
    "February": '02',
    "March": '03',
    "April": '04',
    "May": '05',
    "June": '06',
    "July": '07',
    "August": '08',
    "September": '09',
    "October": 10,
    "November": 11,
    "December": 12}
def for_chan(y,m,d):
    if(str(m).isalpha()):
        if(1 <= int(d) <= 9):
            print(f"Real date: {y}-{ml[m]}-0{d}")
        else:
            print(f"Real date: {y}-{ml[m]}-{d}")
    else:
        if(1 <= d <= 9):
            temp = d
            d = "0" + str(temp)
        if(1 <= m <= 9):
            temp = m
            m = "0" + str(temp)
        print(f"Real date: {y}-{m}-{d}")

while True:
    x = input("Date: ")
    try:
        if "/" in x:
            m,d,y = map(int, x.split('/'))
        else:
            m,d,y = map(str, x.split())
            if m in ml:
                m = m
            d = d.strip(",")
        for_chan(y,m,d)
        break
    
    except (ValueError, KeyError):
        pass

    