from mpi4py import MPI
import time

def calculate_squares(start, end):
    return [i**2 for i in range(start, end)]

start_time = time.time()
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

# Assuming 4 processes in total
numbers_per_process = int(5e8) // size
# 1e7
start_index = rank * numbers_per_process
end_index = start_index + numbers_per_process

partial_squares = calculate_squares(start_index, end_index)

# Gather all partial results to the root process
all_squares = comm. gather(partial_squares, root=0)

if rank == 0:
    # Flatten the list of lists
    final_squares = []
    for part in all_squares:
        final_squares.extend(part)
        # final_squares" [item for sublist in all_squares for item in sublist]
        # print(final_squares)
        end_time = time.time()
        print(f"It took (end_time - start_time) seconds to run this")