import random as r
import matplotlib.pyplot as plt
f = []
for i in range(100):
    list = []
    for i in range(6):
        t = r.randint(0,1)
        list.append(t)
    f.append(list)

print(f)