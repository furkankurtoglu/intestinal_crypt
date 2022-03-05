import mechanica as m
import numpy as np


# potential cutoff distance
cutoff = 0.5

# dimensions of universe
dim=np.array([30., 30., 30.])
center = dim / 2


# new simulator
m.Simulator(dim=dim, cutoff=cutoff)

# adding Cuboid to Universe
c = m.Cuboid(m.Universe.center + [0, 0, 0], size=[30, 30, 5])


# iPython run command
m.irun() 
