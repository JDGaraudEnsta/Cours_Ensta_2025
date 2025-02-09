from builtins import print as seq_print
from mpi4py import MPI

my_comm = MPI.COMM_WORLD.Dup()

rank, size = my_comm.rank, my_comm.size

def print(*args, **kwargs):
    seq_print(f"[{rank:02d}/{size:02d}]", *args, **kwargs)


print("Hello")
