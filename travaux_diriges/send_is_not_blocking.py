from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD

imax=17

if comm.rank == 0:
    for i in range(1, imax):
        time.sleep(.5)
        sz = 2**i
        x = np.ones(sz, dtype=np.int32)
        comm.Send(x, dest=1)
        print("I just sent", sz)

else:
    time.sleep(10)
    print("That was a good nap, let's receive...")
    for i in range(1, imax):
        sz = 2**i
        x = np.empty(sz, dtype=np.int32)
        comm.Recv(x, source=0)
        print("I just received", sz)
