import random as r
import matplotlib.pyplot as plt
import pandas as pd

#LS is the lifespan without food, N is the initial population, P contains all the population
LS = 100
N = 5
P = [[LS] for n in range(N)]

# T is the no. of iterations
T = 3000
PLog = []
FoodLog = []
food = 500
BirthProb = 0.008
for Tloop in range(T):    
    food += 20
    EatingProb = 0.07 * food/len(P)

    new = 0
    deaths = []
    for n in range(len(P)):
        
        if r.random() < BirthProb:
            new += 1

        P[n][0] -= 1
        if (r.random() < EatingProb) & (P[n][0] <= 1) & (food > 0):
            food -= 1
            P[n][0] = LS


        if P[n][0] <= 0:
            deaths.append(n)

    for dead in reversed(deaths):
        P.pop(dead)

    for birth in range(new):
        P.append([LS])

    print(f"P: {len(P)}, t: {Tloop}, Food: {food}")
    PLog.append(len(P))
    FoodLog.append(food)

datacsv = pd.DataFrame([PLog, FoodLog])
datacsv.to_csv("data.csv")

W, graph = plt.subplots()
graph.plot(range(len(PLog)), PLog)
graph.plot(range(len(FoodLog)), FoodLog)
plt.show()