from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()  # number of processes
rank = MPI.COMM_WORLD.Get_rank()  # id of process
name = MPI.Get_processor_name()  # name of processor
msg = "Hello World! I am process {0} of {1} on {2}."
print(msg.format(rank, size, name))
