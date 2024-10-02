import random
import matplotlib.pyplot as plt


bankot = []
runs = 50
time = [t for t in range(runs)]
figure, axis = plt.subplots(5, 5)
for i in range(25):
    half = [0 for i in range(18)]
    th = [1 for i in range(19+i)]
    half.extend(th)
    third = [0 for i in range(12)]
    nonthird = [1 for i in range(25+i)]
    third.extend(nonthird)

    bank = 640
    bet = 10
    bnk = []
    for t in range(runs):
        br = random.choice(half)
        row = random.choice(third)
        if(br == 0):
            bet = 15
            bank+=(bet+bet)
        else:
            bet = 15
            bank-=bet
        if(row == 0):
            bet = 10
            bank+=(bet+(bet*2))
        else:
            bet = 10
            bank -= bet

        bnk.append(bank)
    bankot.append(bnk)

k=0
for i in range(5):
    for j in range(5):
        axis[i,j].plot(time, bankot[k])
        axis[i,j].plot("u = "+str(k))
        k+=1
plt.show()