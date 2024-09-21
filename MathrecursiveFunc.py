

def findnum(p,g):
    x = 1
    y = 0
    t = 1
    while(x > p):
        if (y >= g):
            t+=1
            x = t
            y = 0
        x*=2
        y+=1

    return y
print(findnum(635, 6))