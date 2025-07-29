import random as r
import matplotlib.pyplot as plt
import pandas as pd

#LS is the lifespan without food, N is the initial population, P contains all the population
LS = 100
N = 5
P = [[LS] for n in range(N)]

# T is the no. of iterations
T = 5000
# logging the values to graph them
PLog = []
FoodLog = []
food = 500
# the probability of reproduction for the individual
BirthProb = 0.008
for Tloop in range(T):
    food += 20
    #the probability of finding food is negatively affected by scarcity
    EatingProb = 0.07 * food/len(P)

    new = 0
    deaths = []
    for n in range(len(P)):
        #if a random [0-1] no. is smaller BirthProb a new individual is born
        if r.random() < BirthProb:
            new += 1

        P[n][0] -= 1
        #individuals eat when hungry and food is available
        if (r.random() < EatingProb) & (P[n][0] <= 1) & (food > 0):
            food -= 1
            P[n][0] = LS

        if P[n][0] <= 0:
            deaths.append(n)

    ''' since the previous 'for' loop depends on len(P),
    we should only add or remove individuals outside of it'''
    for dead in reversed(deaths):
        P.pop(dead)

    for birth in range(new):
        P.append([LS])

    if Tloop % 100 == 0:
        print(f"P: {len(P)}, t: {Tloop}, Food: {food}")
    
    #updating logs
    PLog.append(len(P))
    FoodLog.append(food)

#saving the most recent logs
datacsv = pd.DataFrame([PLog, FoodLog])
datacsv.to_csv("data.csv")

#plotting
W, graph = plt.subplots()
graph.plot(range(len(PLog)), PLog)
graph.plot(range(len(FoodLog)), FoodLog)
plt.show()