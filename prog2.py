from mpi4py import MPI
import time


def calculate_squares(start, end):
    return [i**2 for i in range(start, end)]


start_time = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

numbers_per_process = int(1e5)//size

start_index = rank * numbers_per_process
end_index = start_index + numbers_per_process

partial_squares = calculate_squares(start_index, end_index)

all_squares = comm.gather(partial_squares, root=0)

if rank == 0:
    final_square = []
    for part in all_squares:
        final_square.extend(part)
        
        end_time = time.time()
        print(f"It took {end_time-start_time} seconds to run this")