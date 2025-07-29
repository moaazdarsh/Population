import random as r
import matplotlib.pyplot as plt

#LS is the lifespan without food, N is the initial population, P contains all the population
LS = 100
N = 5
P = [[LS] for n in range(N)]

#setting up graphics
W, graph = plt.subplots()
animate = True # set to True to animate the graph

# T is the no. of iterations
T = 5000
# logging the values to graph them
PLog = []
FoodLog = []
food = 500
# the probability of reproduction for the individual
BirthProb = 0.008
for Tloop in range(T):
    food += r.randint(0, 20)

    #the probability of finding food is negatively affected by scarcity
    if len(P) != 0:
        EatingProb = 0.07 * food/len(P)
    else:
        EatingProb = 0
    
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
    for dead in reversed(deaths): #reversed to avoid index errors
        P.pop(dead)

    for birth in range(new):
        P.append([LS])
    

    if Tloop % 100 == 0:
        print(f"P: {len(P)}, t: {Tloop}, Food: {food}")

    #animation 
    if animate:
        graph.clear()
        graph.plot(range(len(PLog)), PLog)
        graph.plot(range(len(FoodLog)), FoodLog)
        plt.show(block=False)
        plt.pause(0.01)

    #updating logs
    PLog.append(len(P))
    FoodLog.append(food)

if not animate:
    #if not animating, show the final graph
    graph.plot(range(len(PLog)), PLog)
    graph.plot(range(len(FoodLog)), FoodLog)
    plt.show()