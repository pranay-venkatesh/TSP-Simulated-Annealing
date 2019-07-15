"""

Solving TSP using Simulated Annealing

Author : Pranay Venkatesh

Oh, ya, the cities are replaced with planets and the salesman is an Imperial Fleet trying to save fuel.

"""

import numpy as np
from random import shuffle, randint, uniform

tour = []

class Planet:
    def __init__ (self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        tour.append(self)
        
# Defining the planets that the space-ship delivers to and randomising the initial tour

def set_planets():
    c1 = Planet(60, 200, "Kashyyyk")
    c2 = Planet(180, 200, "Dagobah")
    c3 = Planet(80, 180, "Mon Calamari")
    c4 = Planet(140, 180, "Utapau")
    c5 = Planet(20, 160, "Tatooine")
    c6 = Planet(100, 160, "Kamino")
    c7 = Planet(200, 160, "Bespin")
    c8 = Planet(140, 140, "Yaavin")
    c9 = Planet(40, 120, "Geonosis")
    c10 = Planet(100, 120, "Ryloth")
    c11 = Planet(180, 100, "Mustafar")
    c12 = Planet(60, 80, "Bespin")
    shuffle(tour)
    
# Probability that a given solution after swapping is acceptable for the next iteration

def accept_probability (curr_d, new_d, T):
    if new_d < curr_d:
        return 1
    return np.exp((curr_d - new_d)/T)
        
def distance(p1, p2):
    return np.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))

def get_total_distance(t):
    d = 0
    for i in range(len(t)-1):
        d += distance(t[i], t[i+1])
    return d

def print_names():
    for planet in tour:
        print (planet.name, end = " ")
    print()

set_planets()


Temperature = 10000
coolingRate = 0.03

print (f"Initial distance of traversal {get_total_distance(tour)}")
print_names()
# print(len(tour))
while (Temperature > 1):
    i1 = randint(0, (len(tour)-1))
    i2 = randint(0, (len(tour)-1))

    new_sol = tour.copy()

    #print(len(new_sol))
    new_sol[i1] = tour[i2]
    new_sol[i2] = tour[i1]
    
    # If the solution is better, update the tour
    
    if accept_probability (curr_d = get_total_distance(tour), new_d = get_total_distance(new_sol), T = Temperature) > uniform(0,1):
        tour = new_sol.copy()
    
    Temperature *= (1 - coolingRate)
    
    
print (f"Final distance of traversal {get_total_distance(tour)}")
print_names()
