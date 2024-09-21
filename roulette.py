import random as r
import matplotlib.pyplot as plt
current = []
time = []
f = []
avgf = []
losewin = []
for j in range(100):
    i = 0
    bank = 640
    bet = 10
    winlose = 0
    while(bank < (640*2) or bank > bet):
        winlose = r.randint(0,1)
        current.append(bank)
        time.append(i)
        if(winlose == 0):
            bank -= bet
            bet *= 2
        else:
            bank += bet
            bet = 10
        i+=1
        print(i)
    f.append(i)
    if(bank < bet):
        losewin.append("lose")
    else:
        losewin.append("win")
#plt.plot(time, current)
plt.hist(losewin)
plt.show()